# TN Foster Care Youth Dataset Analysis

This project provides a comprehensive analytic approach and implementation for analyzing the "IL YOUTH DATASET FROM FY23-25.xlsx" file, which contains assessment data for 5,684 youth in the Tennessee foster care system.

## Project Overview

The analysis focuses on understanding geographic distribution and vulnerabilities across three critical domains:
- **Housing Stability**: Living situation, independent living skills, residential stability
- **Mental Health**: Depression, anxiety, trauma, substance use, and other mental health indicators
- **Supportive Adult Relationships**: Family strengths, social connectedness, attachment patterns

## Files Description

### 1. `Analytic_Approach_Document.md`
A comprehensive document outlining the analytic framework, methodology, and expected outcomes for the TN foster care youth analysis.

**Key Sections:**
- Dataset overview and structure
- Vulnerability assessment framework
- Geographic analysis methodology
- Timeline and deliverables
- Risk mitigation strategies

### 2. `analysis_implementation.py`
A Python script that implements the key analytic components outlined in the approach document.

**Features:**
- Data loading and cleaning
- Vulnerability scoring by domain
- Geographic aggregation (county and zip code levels)
- Pattern analysis across vulnerability domains
- High-need area identification
- Data visualization
- Report generation

**Output Files Generated:**
- `youth_vulnerability_summary.csv`: Individual youth vulnerability profiles
- `county_vulnerability_summary.csv`: County-level vulnerability summaries
- `zip_vulnerability_summary.csv`: Zip code-level vulnerability summaries
- `vulnerability_analysis_visualizations.png`: Analysis charts and graphs

### 3. `requirements.txt`
Lists all Python package dependencies required to run the analysis script.

### 4. `notebooks/data checks.ipynb`
Jupyter notebook containing initial data exploration and structure analysis.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone or download the project files**
2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the Excel dataset is in the correct location:**
   - Place `IL YOUTH DATASET FROM FY23-25.xlsx` in the `data/` folder
   - The file should contain a sheet named "Dataset"

## Usage

### Running the Analysis

1. **Execute the main analysis script:**
   ```bash
   python analysis_implementation.py
   ```

2. **The script will:**
   - Load and process the dataset
   - Calculate vulnerability scores for each domain
   - Create geographic summaries
   - Generate visualizations
   - Save processed data to CSV files
   - Display a comprehensive analysis report

### Customizing the Analysis

You can modify the `analysis_implementation.py` script to:
- Adjust vulnerability scoring thresholds
- Add new assessment indicators to domains
- Modify visualization parameters
- Change output file formats

## Data Structure Understanding

### Dataset Characteristics
- **Total Records**: 557,897 assessment responses
- **Unique Youth**: 5,684 individuals
- **Assessment Types**: CANS (Child and Adolescent Needs and Strengths) and LIFESKILL
- **Geographic Coverage**: 96 counties across Tennessee
- **Time Period**: FY23-25 (Fiscal Years 2023-2025)

### Key Variables
- **Demographics**: PERSON ID, CURRENT AGE, GENDER
- **Geographic**: COMMITMENT COUNTY, RESPONSIBLE COUNTY, REMOVAL ZIP CODE, PLACEMENT ZIP CODE
- **Assessment**: ASSESSMENT TYPE, ASSESSMENT INDICATOR, SCORE-RESULT, GENERAL RESULT DESCRIPTION

### Scoring System
- **0**: No current need (stable/healthy)
- **1**: Mild problems requiring monitoring
- **2**: Action required (interfering with functioning)
- **3**: Dangerous/disabled requiring immediate action

## Expected Outcomes

### Geographic Insights
- Identification of high-need counties and regions
- Understanding of urban vs. rural vulnerability patterns
- Mapping of service gaps and resource needs

### Vulnerability Patterns
- Correlation between housing, mental health, and relationship vulnerabilities
- Age-related vulnerability trends
- Gender-based vulnerability differences

### Policy Implications
- Resource allocation recommendations
- Service delivery optimization
- Prevention and intervention targeting

## Troubleshooting

### Common Issues

1. **File not found error:**
   - Ensure the Excel file is in the `data/` folder
   - Check that the filename matches exactly

2. **Package import errors:**
   - Verify all requirements are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

3. **Memory issues with large datasets:**
   - The script processes data in chunks to manage memory
   - Consider running on a machine with sufficient RAM

### Data Quality Notes
- Some geographic fields may contain missing values
- Assessment indicators use partial string matching
- Scores are averaged when multiple assessments exist for the same indicator

## Contributing

To extend or modify the analysis:
1. Review the `Analytic_Approach_Document.md` for methodology
2. Modify the `analysis_implementation.py` script as needed
3. Update the requirements.txt if new packages are added
4. Test with the dataset to ensure functionality

## Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the analytic approach document for methodology details
3. Examine the data structure using the provided notebook

## License

This project is provided as-is for educational and research purposes. Please ensure compliance with data privacy and governance requirements when working with foster care data.
