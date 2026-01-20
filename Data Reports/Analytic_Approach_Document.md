# Analytic Approach Document: TN Foster Care Youth Dataset Analysis

## Executive Summary




This document outlines the analytic approach for analyzing the "IL YOUTH DATASET FROM FY23-25.xlsx" file, which contains comprehensive assessment data for 5,684 youth in the Tennessee foster care system. The analysis will focus on understanding geographic distribution and vulnerabilities across three critical domains: Housing Stability, Mental Health, and Supportive Adult Relationships.

## Dataset Overview

### Structure
- **Total Records**: 557,897 assessment responses
- **Unique Youth**: 5,684 individuals
- **Time Period**: FY23-25 (Fiscal Years 2023-2025)
- **Assessment Types**: 
  - CANS (Child and Adolescent Needs and Strengths): 514,657 records
  - LIFESKILL: 43,240 records
- **Geographic Coverage**: 96 counties across Tennessee

### Key Variables
- **Demographics**: PERSON ID, CURRENT AGE, GENDER
- **Geographic**: COMMITMENT COUNTY, RESPONSIBLE COUNTY, REMOVAL ZIP CODE, PLACEMENT ZIP CODE
- **Assessment**: ASSESSMENT TYPE, ASSESSMENT INDICATOR, SCORE-RESULT, GENERAL RESULT DESCRIPTION
- **Temporal**: LOCATION BEGIN DATE, LOCATION END DATE

## Analytic Framework

### 1. Geographic Distribution Analysis

#### 1.1 County-Level Analysis
- **Primary Focus**: COMMITMENT COUNTY (96 unique counties)
- **Secondary**: RESPONSIBLE COUNTY for cross-reference
- **Methodology**: 
  - Count unique youth per county
  - Calculate youth density per county population
  - Identify geographic clusters and outliers

#### 1.2 Zip Code Analysis
- **Removal vs. Placement**: Compare REMOVAL ZIP CODE vs. PLACEMENT ZIP CODE
- **Geographic Mobility**: Analyze distance between removal and placement locations
- **Urban vs. Rural**: Categorize zip codes by population density

#### 1.3 Regional Clustering
- **East Tennessee**: Knox, Sevier, Sullivan counties
- **Middle Tennessee**: Davidson, Rutherford, Williamson counties  
- **West Tennessee**: Shelby, Madison, Fayette counties

### 2. Vulnerability Assessment Framework

#### 2.1 Housing Stability Domain

**Key Indicators to Analyze:**
- Living Situation
- Independent Living Skills
- Youth Residential Stability
- Housing Plan Identification
- Backup Housing Plan
- Housing Education and Training

**Scoring Interpretation:**
- **0**: No current need (stable housing)
- **1**: Mild problems requiring monitoring
- **2**: Action required (interfering with functioning)
- **3**: Dangerous/disabled requiring immediate action

**Analytic Questions:**
- What percentage of youth have stable housing plans?
- How do housing vulnerabilities vary by age and location?
- Are there geographic disparities in housing stability?

#### 2.2 Mental Health Domain

**Key Indicators to Analyze:**
- Depression
- Anxiety
- Trauma-related symptoms (PTSD, adjustment disorders)
- Psychotic symptoms
- Substance use
- Suicidal ideation/self-harm
- Developmental/Intellectual challenges

**Scoring Interpretation:**
- **0**: No evidence of problems
- **1**: History/suspicion requiring monitoring
- **2**: Clear evidence requiring intervention
- **3**: Dangerous/disabled requiring immediate action

**Analytic Questions:**
- What is the prevalence of mental health needs by region?
- How do mental health vulnerabilities correlate with housing stability?
- Are there geographic gaps in mental health service access?

#### 2.3 Supportive Adult Relationships Domain

**Key Indicators to Analyze:**
- Family Strengths
- Interpersonal/Social Connectedness
- Relationship Permanence
- Family Functioning
- Social Functioning
- Attachment Difficulties
- Caregiver Relationships

**Scoring Interpretation:**
- **0**: No evidence of problems
- **1**: Mild problems requiring monitoring
- **2**: Problems interfering with functioning
- **3**: Dangerous/disabled requiring immediate action

**Analytic Questions:**
- How do relationship strengths vary geographically?
- What is the correlation between relationship stability and other vulnerabilities?
- Are there regional differences in family support systems?

### 3. Methodology

#### 3.1 Data Preparation
1. **Data Cleaning**:
   - Handle missing values in geographic fields
   - Standardize assessment indicator names
   - Convert score results to numeric where possible

2. **Data Aggregation**:
   - Create youth-level summaries for each vulnerability domain
   - Aggregate scores by county and zip code
   - Calculate vulnerability indices for each domain

#### 3.2 Vulnerability Scoring
1. **Domain-Specific Indices**:
   - Housing Stability Index: Average of housing-related assessment scores
   - Mental Health Index: Average of mental health assessment scores
   - Relationship Index: Average of relationship assessment scores

2. **Composite Vulnerability Score**:
   - Weighted combination of all three domains
   - Normalize scores for geographic comparison

#### 3.3 Geographic Analysis
1. **Spatial Distribution**:
   - Choropleth maps by county
   - Heat maps by zip code
   - Identify high-need geographic clusters

2. **Regional Comparisons**:
   - East vs. Middle vs. West Tennessee
   - Urban vs. rural areas
   - Border counties vs. interior counties

### 4. Expected Outcomes

#### 4.1 Geographic Insights
- Identification of high-need counties and regions
- Understanding of urban vs. rural vulnerability patterns
- Mapping of service gaps and resource needs

#### 4.2 Vulnerability Patterns
- Correlation between housing, mental health, and relationship vulnerabilities
- Age-related vulnerability trends
- Gender-based vulnerability differences

#### 4.3 Policy Implications
- Resource allocation recommendations
- Service delivery optimization
- Prevention and intervention targeting

### 5. Deliverables

#### 5.1 Data Products
- County-level vulnerability dashboard
- Zip code-level vulnerability maps
- Youth-level vulnerability profiles

#### 5.2 Analysis Reports
- Geographic vulnerability analysis
- Cross-domain correlation analysis
- Policy recommendations report

#### 5.3 Visualization Tools
- Interactive maps showing vulnerability by location
- Trend analysis charts
- Comparative analysis dashboards

### 6. Technical Requirements

#### 6.1 Data Processing
- Python/R for data manipulation
- Geographic information systems (GIS) for mapping
- Statistical analysis packages for correlation analysis

#### 6.2 Visualization
- Tableau/Power BI for dashboards
- Python libraries (matplotlib, seaborn, plotly) for charts
- GIS software for geographic visualizations

#### 6.3 Data Storage
- Structured database for processed data
- Version control for analysis scripts
- Documentation of data transformations

### 7. Timeline and Milestones

#### Phase 1: Data Exploration (Week 1-2)
- Complete data structure analysis
- Identify all relevant assessment indicators
- Create initial data quality report

#### Phase 2: Vulnerability Scoring (Week 3-4)
- Develop vulnerability indices
- Create youth-level vulnerability profiles
- Validate scoring methodology

#### Phase 3: Geographic Analysis (Week 5-6)
- Generate county and zip code level summaries
- Create geographic visualizations
- Identify spatial patterns and clusters

#### Phase 4: Cross-Domain Analysis (Week 7-8)
- Analyze correlations between vulnerability domains
- Develop composite vulnerability measures
- Create comprehensive vulnerability profiles

#### Phase 5: Reporting and Visualization (Week 9-10)
- Generate final analysis reports
- Create interactive dashboards
- Develop policy recommendations

### 8. Risk Mitigation

#### 8.1 Data Quality
- Validate assessment scoring consistency
- Handle missing geographic data appropriately
- Document data limitations and assumptions

#### 8.2 Methodological Challenges
- Ensure vulnerability scoring is clinically meaningful
- Address geographic boundary issues
- Validate statistical significance of findings

#### 8.3 Privacy and Security
- Maintain youth confidentiality
- Aggregate data to appropriate geographic levels
- Follow data governance protocols

## Conclusion

This analytic approach provides a comprehensive framework for understanding the geographic distribution and vulnerabilities of youth in the Tennessee foster care system. By focusing on housing stability, mental health, and supportive adult relationships, the analysis will identify critical service gaps and inform resource allocation decisions to better support vulnerable youth across the state.

The methodology emphasizes both geographic and vulnerability domain analysis, ensuring that findings are actionable for policymakers and service providers. The expected deliverables will provide multiple levels of insight, from individual youth profiles to regional policy recommendations.
