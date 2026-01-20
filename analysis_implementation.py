#!/usr/bin/env python3
"""
TN Foster Care Youth Dataset Analysis Implementation
This script demonstrates the key analytic components outlined in the Analytic Approach Document.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

class FosterCareAnalyzer:
    """
    Main class for analyzing TN foster care youth dataset
    """
    
    def __init__(self, file_path):
        """
        Initialize the analyzer with the dataset
        
        Args:
            file_path (str): Path to the Excel file
        """
        self.file_path = file_path
        self.df = None
        self.youth_summary = None
        self.county_summary = None
        self.zip_summary = None
        
        # Define vulnerability domains and their indicators
        self.vulnerability_domains = {
            'housing_stability': [
                'Living Situation', 'Independent Living Skills', 'Youth Residential Stability',
                'Housing Plan', 'Backup Housing Plan', 'Housing Education'
            ],
            'mental_health': [
                'Depression', 'Anxiety', 'Trauma', 'PTSD', 'Substance Use',
                'Suicidal Ideation', 'Self-Injury', 'Psychotic Symptoms'
            ],
            'supportive_relationships': [
                'Family Strengths', 'Interpersonal/Social Connectedness', 'Relationship Permanence',
                'Family Functioning', 'Social Functioning', 'Attachment Difficulties'
            ]
        }
        
        # Define scoring interpretation
        self.scoring_interpretation = {
            0: 'No current need',
            1: 'Mild problems requiring monitoring', 
            2: 'Action required',
            3: 'Dangerous/disabled requiring immediate action'
        }
        
    def load_data(self):
        """Load and prepare the dataset"""
        print("Loading dataset...")
        
        # Load the Excel file
        self.df = pd.read_excel(
            self.file_path, 
            sheet_name='Dataset',
            dtype={
                'PERSON ID': str, 
                'REMOVAL ZIP CODE': str, 
                'PLACEMENT ZIP CODE': str
            }
        )
        
        print(f"Dataset loaded: {self.df.shape[0]} records, {self.df.shape[1]} columns")
        print(f"Unique youth: {self.df['PERSON ID'].nunique()}")
        
        # Basic data cleaning
        self.df['SCORE-RESULT'] = pd.to_numeric(self.df['SCORE-RESULT'], errors='coerce')
        
        return self.df
    
    def create_youth_summary(self):
        """Create youth-level summary with vulnerability scores"""
        print("Creating youth-level vulnerability summaries...")
        
        youth_data = []
        
        for person_id in self.df['PERSON ID'].unique():
            person_df = self.df[self.df['PERSON ID'] == person_id]
            
            # Get basic demographics
            youth_info = {
                'PERSON ID': person_id,
                'CURRENT AGE': person_df['CURRENT AGE'].iloc[0],
                'GENDER': person_df['GENDER'].iloc[0],
                'COMMITMENT COUNTY': person_df['COMMITMENT COUNTY'].iloc[0],
                'RESPONSIBLE COUNTY': person_df['RESPONSIBLE COUNTY'].iloc[0],
                'REMOVAL ZIP CODE': person_df['REMOVAL ZIP CODE'].iloc[0],
                'PLACEMENT ZIP CODE': person_df['PLACEMENT ZIP CODE'].iloc[0]
            }
            
            # Calculate vulnerability scores for each domain
            for domain, indicators in self.vulnerability_domains.items():
                domain_scores = []
                
                for indicator in indicators:
                    # Find matching assessment indicators (partial matching)
                    matching_indicators = person_df[
                        person_df['ASSESSMENT INDICATOR'].str.contains(
                            indicator, case=False, na=False
                        )
                    ]
                    
                    if not matching_indicators.empty:
                        scores = matching_indicators['SCORE-RESULT'].dropna()
                        if not scores.empty:
                            domain_scores.extend(scores.tolist())
                
                # Calculate domain vulnerability score
                if domain_scores:
                    youth_info[f'{domain}_score'] = np.mean(domain_scores)
                    youth_info[f'{domain}_count'] = len(domain_scores)
                else:
                    youth_info[f'{domain}_score'] = np.nan
                    youth_info[f'{domain}_count'] = 0
            
            youth_data.append(youth_info)
        
        self.youth_summary = pd.DataFrame(youth_data)
        
        # Calculate composite vulnerability score
        domain_cols = [col for col in self.youth_summary.columns if col.endswith('_score')]
        self.youth_summary['composite_vulnerability'] = self.youth_summary[domain_cols].mean(axis=1)
        
        print(f"Youth summary created: {len(self.youth_summary)} youth profiles")
        return self.youth_summary
    
    def create_geographic_summaries(self):
        """Create county and zip code level summaries"""
        print("Creating geographic summaries...")
        
        # County-level summary
        self.county_summary = self.youth_summary.groupby('COMMITMENT COUNTY').agg({
            'PERSON ID': 'count',
            'housing_stability_score': ['mean', 'std', 'count'],
            'mental_health_score': ['mean', 'std', 'count'],
            'supportive_relationships_score': ['mean', 'std', 'count'],
            'composite_vulnerability': ['mean', 'std']
        }).round(3)
        
        # Flatten column names
        self.county_summary.columns = ['_'.join(col).strip() for col in self.county_summary.columns]
        self.county_summary = self.county_summary.reset_index()
        
        # Zip code level summary (removal zip codes)
        self.zip_summary = self.youth_summary.groupby('REMOVAL ZIP CODE').agg({
            'PERSON ID': 'count',
            'composite_vulnerability': ['mean', 'std']
        }).round(3)
        
        self.zip_summary.columns = ['_'.join(col).strip() for col in self.zip_summary.columns]
        self.zip_summary = self.zip_summary.reset_index()
        
        print(f"County summary: {len(self.county_summary)} counties")
        print(f"Zip code summary: {len(self.zip_summary)} zip codes")
        
        return self.county_summary, self.zip_summary
    
    def analyze_vulnerability_patterns(self):
        """Analyze patterns across vulnerability domains"""
        print("Analyzing vulnerability patterns...")
        
        # Correlation analysis between domains
        domain_cols = ['housing_stability_score', 'mental_health_score', 'supportive_relationships_score']
        correlation_matrix = self.youth_summary[domain_cols].corr()
        
        print("\nVulnerability Domain Correlations:")
        print(correlation_matrix.round(3))
        
        # Age-based vulnerability analysis
        age_vulnerability = self.youth_summary.groupby('CURRENT AGE')[domain_cols + ['composite_vulnerability']].mean()
        
        print("\nVulnerability by Age:")
        print(age_vulnerability.round(3))
        
        # Gender-based vulnerability analysis
        gender_vulnerability = self.youth_summary.groupby('GENDER')[domain_cols + ['composite_vulnerability']].mean()
        
        print("\nVulnerability by Gender:")
        print(gender_vulnerability.round(3))
        
        return correlation_matrix, age_vulnerability, gender_vulnerability
    
    def identify_high_need_areas(self, threshold_percentile=75):
        """Identify high-need counties and zip codes"""
        print(f"Identifying high-need areas (top {100-threshold_percentile}%)...")
        
        # High-need counties
        threshold = self.county_summary['composite_vulnerability_mean'].quantile(threshold_percentile/100)
        high_need_counties = self.county_summary[
            self.county_summary['composite_vulnerability_mean'] >= threshold
        ].sort_values('composite_vulnerability_mean', ascending=False)
        
        print(f"\nHigh-need counties (vulnerability score >= {threshold:.3f}):")
        print(high_need_counties[['COMMITMENT COUNTY', 'PERSON ID_count', 'composite_vulnerability_mean']].head(10))
        
        # High-need zip codes
        zip_threshold = self.zip_summary['composite_vulnerability_mean'].quantile(threshold_percentile/100)
        high_need_zips = self.zip_summary[
            self.zip_summary['composite_vulnerability_mean'] >= zip_threshold
        ].sort_values('composite_vulnerability_mean', ascending=False)
        
        print(f"\nHigh-need zip codes (vulnerability score >= {zip_threshold:.3f}):")
        print(high_need_zips[['REMOVAL ZIP CODE', 'PERSON ID_count', 'composite_vulnerability_mean']].head(10))
        
        return high_need_counties, high_need_zips
    
    def create_visualizations(self):
        """Create basic visualizations for the analysis"""
        print("Creating visualizations...")
        
        # Set up the plotting style
        plt.style.use('seaborn-v0_8')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('TN Foster Care Youth Vulnerability Analysis', fontsize=16)
        
        # 1. Vulnerability distribution by county
        top_counties = self.county_summary.nlargest(15, 'composite_vulnerability_mean')
        axes[0, 0].barh(range(len(top_counties)), top_counties['composite_vulnerability_mean'])
        axes[0, 0].set_yticks(range(len(top_counties)))
        axes[0, 0].set_yticklabels(top_counties['COMMITMENT COUNTY'])
        axes[0, 0].set_xlabel('Composite Vulnerability Score')
        axes[0, 0].set_title('Top 15 Counties by Vulnerability Score')
        
        # 2. Vulnerability by age
        age_data = self.youth_summary.groupby('CURRENT AGE')['composite_vulnerability'].mean()
        axes[0, 1].plot(age_data.index, age_data.values, marker='o')
        axes[0, 1].set_xlabel('Age')
        axes[0, 1].set_ylabel('Average Vulnerability Score')
        axes[0, 1].set_title('Vulnerability by Age')
        axes[0, 1].grid(True)
        
        # 3. Domain correlation heatmap
        domain_cols = ['housing_stability_score', 'mental_health_score', 'supportive_relationships_score']
        corr_data = self.youth_summary[domain_cols].corr()
        sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0, ax=axes[1, 0])
        axes[1, 0].set_title('Vulnerability Domain Correlations')
        
        # 4. Geographic distribution of youth
        county_counts = self.youth_summary['COMMITMENT COUNTY'].value_counts().head(15)
        axes[1, 1].barh(range(len(county_counts)), county_counts.values)
        axes[1, 1].set_yticks(range(len(county_counts)))
        axes[1, 1].set_yticklabels(county_counts.index)
        axes[1, 1].set_xlabel('Number of Youth')
        axes[1, 1].set_title('Top 15 Counties by Youth Count')
        
        plt.tight_layout()
        plt.savefig('auto_results/vulnerability_analysis_visualizations.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Visualizations saved as 'auto_results/vulnerability_analysis_visualizations.png'")
    
    def generate_report(self):
        """Generate a summary report of the analysis"""
        print("\n" + "="*80)
        print("TN FOSTER CARE YOUTH VULNERABILITY ANALYSIS REPORT")
        print("="*80)
        
        print(f"\nDataset Overview:")
        print(f"- Total youth analyzed: {len(self.youth_summary):,}")
        print(f"- Counties represented: {len(self.county_summary):,}")
        print(f"- Zip codes represented: {len(self.zip_summary):,}")
        
        print(f"\nVulnerability Score Summary:")
        print(f"- Housing Stability: Mean = {self.youth_summary['housing_stability_score'].mean():.3f}")
        print(f"- Mental Health: Mean = {self.youth_summary['mental_health_score'].mean():.3f}")
        print(f"- Supportive Relationships: Mean = {self.youth_summary['supportive_relationships_score'].mean():.3f}")
        print(f"- Composite Vulnerability: Mean = {self.youth_summary['composite_vulnerability'].mean():.3f}")
        
        print(f"\nGeographic Distribution:")
        print(f"- County with most youth: {self.county_summary.loc[self.county_summary['PERSON ID_count'].idxmax(), 'COMMITMENT COUNTY']}")
        print(f"- County with highest vulnerability: {self.county_summary.loc[self.county_summary['composite_vulnerability_mean'].idxmax(), 'COMMITMENT COUNTY']}")
        
        print(f"\nKey Findings:")
        print(f"- {len(self.youth_summary[self.youth_summary['composite_vulnerability'] > 1.5])} youth have high vulnerability scores (>1.5)")
        print(f"- {len(self.county_summary[self.county_summary['composite_vulnerability_mean'] > 1.0])} counties have average vulnerability scores >1.0")
        
        print("\n" + "="*80)

def main():
    """Main execution function"""
    print("TN Foster Care Youth Dataset Analysis")
    print("="*50)
    
    # Initialize analyzer
    analyzer = FosterCareAnalyzer('data/IL YOUTH DATASET FROM FY23-25.xlsx')
    
    try:
        # Load data
        analyzer.load_data()
        
        # Create youth summaries
        analyzer.create_youth_summary()
        
        # Create geographic summaries
        analyzer.create_geographic_summaries()
        
        # Analyze patterns
        analyzer.analyze_vulnerability_patterns()
        
        # Identify high-need areas
        analyzer.identify_high_need_areas()
        
        # Create visualizations
        analyzer.create_visualizations()
        
        # Generate report
        analyzer.generate_report()
        
        # Save processed data
        analyzer.youth_summary.to_csv('auto_results/youth_vulnerability_summary.csv', index=False)
        analyzer.county_summary.to_csv('auto_results/county_vulnerability_summary.csv', index=False)
        analyzer.zip_summary.to_csv('auto_results/zip_vulnerability_summary.csv', index=False)
        
        print("\nAnalysis complete! Data files saved:")
        print("- youth_vulnerability_summary.csv")
        print("- county_vulnerability_summary.csv") 
        print("- zip_vulnerability_summary.csv")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
