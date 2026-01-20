# NYTD Data Validation and Cleaning Framework

## Belmont Data Collaborative - AI-First Data Processing Pipeline

### Overview

This framework provides comprehensive validation and cleaning for National Youth in Transition Database (NYTD) Outcomes data, following specifications from the NYTD Codebook and User's Guide. The NYTD tracks outcomes for youth aging out of foster care across three longitudinal waves.

### Datasets Supported

| Dataset | Name | Cohort Year | Waves | FIPS5 Available | Description |
|---------|------|-------------|-------|-----------------|-------------|
| 202 | FY2011 Cohort | 2011 | 1-2-3 | ❌ | First NYTD cohort |
| 228 | FY2014 Cohort | 2014 | 1-2-3 | ❌ | Second NYTD cohort |
| 266 | FY2017 Cohort | 2017 | 1-2-3 | ✅ | Third NYTD cohort |
| 297 | FY2020 Cohort | 2020 | 1-2-3 | ✅ | Fourth NYTD cohort |

### Key Features

#### 🔍 **Comprehensive Validation**
- **Structure Validation**: Verifies expected columns, data types, and dimensions
- **Value Range Validation**: Ensures all values conform to NYTD codebook specifications
- **Logical Consistency**: Validates relationships between variables (e.g., marriage requires children)
- **Temporal Consistency**: Verifies age progressions across waves

#### 🧹 **Intelligent Data Cleaning**
- **Missing Value Analysis**: Comprehensive patterns and imputation strategies
- **Data Type Conversion**: Proper handling of dates, integers, and categorical variables
- **Standardization**: Consistent formatting across datasets and cohorts
- **Derived Variables**: Creation of analysis-ready variables (race/ethnicity, employment status)

#### 📊 **Quality Assessment**
- **Multi-dimensional Scoring**: Completeness, validity, consistency, and overall quality
- **Visual Reports**: Interactive charts and heatmaps for quality assessment
- **Cross-dataset Comparison**: Consistency analysis across multiple cohorts
- **Analysis Readiness**: Scoring system for research-ready data

#### 🔗 **AI-First Approach**
- **Automated Decision Making**: Rule-based corrections and imputations
- **Pattern Recognition**: Identifies systematic missing data patterns
- **Quality Predictions**: Flags potential data collection issues
- **Smart Recommendations**: Context-aware suggestions for data improvements

---

## Quick Start

### 1. Installation and Setup

```python
# Import the framework
from nytd_validation_framework import NYTDDataValidator, process_nytd_dataset
from nytd_dataset_config import create_dataset_specific_validator

# Initialize for a specific dataset
dataset_number = "297"  # FY2020 Cohort
validator = create_dataset_specific_validator(dataset_number)
```

### 2. Basic Processing

```python
# Process a single dataset
df_cleaned, validation_results = process_nytd_dataset(
    dataset_number="297", 
    file_path="nytd_outcomes_297.csv"
)

print(f"Quality Score: {validation_results['data_quality_metrics']['overall_score']:.1f}/100")
```

### 3. Advanced Workflow

```python
# Load and validate data structure
df_raw = validator.load_data_from_s3("nytd_outcomes_297.csv")
structure_report = validator.validate_data_structure(df_raw)

# Apply type conversions and validations
df_typed = validator.validate_data_types(df_raw)
value_issues = validator.validate_value_ranges(df_typed)

# Analyze missing values and apply corrections
missing_analysis = validator.analyze_missing_values(df_typed)
df_cleaned = validator.apply_data_corrections(df_typed)

# Generate quality report and save results
quality_report = validator.generate_data_quality_report(df_cleaned)
cleaned_path = validator.save_cleaned_data(df_cleaned)
report_path = validator.save_validation_report()
```

---

## Framework Components

### Core Classes

#### `NYTDDataValidator`
Main validation engine with comprehensive rule-based checking.

**Key Methods:**
- `load_data_from_s3()`: Secure data loading from S3 storage
- `validate_data_structure()`: Basic structure and dimension checks
- `validate_data_types()`: Type conversion and validation
- `validate_value_ranges()`: NYTD codebook compliance checking
- `validate_logical_consistency()`: Cross-variable relationship validation
- `analyze_missing_values()`: Pattern detection and imputation planning
- `apply_data_corrections()`: Automated standardization and corrections
- `generate_data_quality_report()`: Multi-dimensional quality assessment

#### `NYTDDatasetConfig`
Dataset-specific configurations and metadata management.

**Features:**
- Dataset metadata and specifications
- Column mapping across cohorts
- Wave-specific validation rules
- Missing value pattern definitions
- Cross-dataset standardization

---

## Validation Rules

### Core Data Elements

| Element | Valid Values | Description |
|---------|-------------|-------------|
| Wave | 1, 2, 3 | Survey wave (Age 17, 19, 21) |
| Sex | 1, 2 | 1=Male, 2=Female |
| Race Variables | 0, 1, 77 | 0=No, 1=Yes, 77=Unknown |
| HisOrgin | 0, 1, 2, 3, 77 | Hispanic ethnicity |
| OutcmRpt | 1-9, 77 | Outcomes reporting status |

### Outcome Variables (Elements 37-58)

| Category | Variables | Valid Values |
|----------|-----------|-------------|
| Employment | CurrFTE, CurrPTE, EmplySklls | 0, 1, 2, 77 |
| Financial Support | SocSecrty, EducAid, PubFinAs, PubFoodAs, PubHousAs, OthrFinAs | 0, 1, 2, 77, 88* |
| Education | HighEdCert, CurrEnroll | Various (see codebook) |
| Life Experiences | Homeless, SubAbuse, Incarc, Children | 0, 1, 2, 77 |
| Health Insurance | Medicaid, OthrHlthIn, MedicalIn, MentlHlthIn, Prescripin | 0, 1, 2, 3, 77, 88* |

*88 = Not Applicable (context-dependent)

### Logical Consistency Rules

1. **Marriage ↔ Children**: If married at child's birth (Marriage=1), must have children (Children=1)
2. **Foster Care ↔ Public Assistance**: If in foster care (OutcmFCS=1), public assistance should be N/A (88)
3. **Age Consistency**: Wave ages should align with cohort year and expected progression
4. **Health Insurance Hierarchy**: Mental health and prescription coverage require medical coverage

---

## Quality Scoring System

### Overall Score Calculation
**Total Score = (Completeness × 0.25) + (Validity × 0.25) + (Consistency × 0.25) + (Readiness × 0.25)**

### Scoring Dimensions

#### 1. Completeness (0-25 points)
- **Core Variables**: StFCID, Wave, DOB, Sex, OutcmFCS
- **Outcome Variables**: Survey response rates for Elements 37-58
- **Calculation**: Percentage of non-missing values

#### 2. Validity (0-25 points)
- **Range Compliance**: Values within NYTD codebook specifications
- **Type Conformance**: Proper data types and formats
- **Calculation**: Percentage of valid values

#### 3. Consistency (0-25 points)
- **Logical Rules**: Cross-variable relationship validation
- **Temporal Patterns**: Age progression and wave consistency
- **Calculation**: Percentage of records passing consistency checks

#### 4. Analysis Readiness (0-25 points)
- **Derived Variables**: Availability of analysis-ready variables
- **Missing Patterns**: Systematic vs. random missingness
- **Documentation**: Data dictionary and metadata completeness

### Quality Thresholds

| Score Range | Quality Level | Recommendation |
|-------------|---------------|----------------|
| 85-100 | 🟢 High Quality | Ready for analysis |
| 70-84 | 🟡 Acceptable | Review warnings before analysis |
| 50-69 | 🟠 Needs Improvement | Address issues before analysis |
| Below 50 | 🔴 Poor Quality | Major data quality concerns - investigate |

---

## Missing Value Strategy

### Pattern Classification

#### 1. **Systematic Missing (Expected)**
- **Code 77 (Blank)**: Youth did not participate in survey
- **Code 88 (Not Applicable)**: Question doesn't apply to youth's situation
- **Example**: Public assistance N/A for youth in foster care

#### 2. **Survey Non-Response**
- **Pattern**: High missingness across outcome variables (Elements 37-58)
- **Cause**: Youth declined to participate or couldn't be located
- **Strategy**: Preserve missingness pattern, create non-response indicators

#### 3. **Item Non-Response**
- **Code 2 (Declined)**: Youth declined specific questions
- **Pattern**: Random across variables, typically <10%
- **Strategy**: Context-aware imputation or analysis adjustment

#### 4. **Administrative Missing**
- **Pattern**: Core variables (demographics, dates) missing
- **Cause**: Data collection or processing errors
- **Strategy**: High priority for correction/imputation

### Imputation Strategies

| Variable Type | Missing % | Strategy | Rationale |
|---------------|-----------|----------|-----------|
| Core Demographics | <5% | Mode/Administrative Lookup | Critical for analysis |
| Core Demographics | >5% | Investigate Data Collection | Likely systematic issue |
| Race Variables | <10% | Multiple Imputation | Geographic/demographic patterns |
| Race Variables | >10% | Missing Category | Systematic non-response |
| Outcome Variables | <20% | Conditional Mode | Similar participant patterns |
| Outcome Variables | >20% | Preserve Pattern | Survey non-response indicator |

---

## File Structure and Outputs

### Input Files
```
s3://bdc-public-raw/ndacan/nytd/outcomes/
├── 202/
│   └── nytd_outcomes_202.csv
├── 228/
│   └── nytd_outcomes_228.csv
├── 266/
│   └── nytd_outcomes_266.csv
└── 297/
    └── nytd_outcomes_297.csv
```

### Output Files
```
s3://bdc-public-curated/ndacan/nytd/outcomes/
├── cleaned/
│   ├── nytd_outcomes_dataset_297_cleaned_20241225_143022.csv
│   └── nytd_297_analysis_ready_20241225_143025.csv
├── validation_reports/
│   ├── nytd_dataset_297_validation_report_20241225_143022.json
│   └── nytd_297_data_dictionary_20241225_143025.json
└── cross_dataset/
    ├── nytd_cross_dataset_comparison_20241225_143030.json
    └── nytd_longitudinal_analysis_dataset_20241225_143035.csv
```

### SharePoint Documentation
```
SharePoint/BelmontDataCollaborative/NYTD_Processing/
├── notebooks/
│   ├── NYTD_Dataset_202_Validation.ipynb
│   ├── NYTD_Dataset_228_Validation.ipynb
│   ├── NYTD_Dataset_266_Validation.ipynb
│   └── NYTD_Dataset_297_Validation.ipynb
├── reports/
│   ├── NYTD_Data_Quality_Summary_20241225.pdf
│   └── NYTD_Cross_Dataset_Analysis_20241225.pdf
└── documentation/
    ├── NYTD_Processing_Guide.md
    └── NYTD_Variable_Mappings.xlsx
```

---

## Advanced Features

### Cross-Dataset Analysis

```python
from nytd_dataset_config import standardize_across_datasets, create_cross_dataset_validation_report

# Load and standardize multiple datasets
datasets = ['202', '228', '266', '297']
dfs = []
for dataset_num in datasets:
    df_cleaned, _ = process_nytd_dataset(dataset_num, f"nytd_outcomes_{dataset_num}.csv")
    dfs.append(df_cleaned)

# Standardize for comparison
standardized_dfs = standardize_across_datasets(dfs, datasets)

# Generate cross-dataset report
comparison_report = create_cross_dataset_validation_report(standardized_dfs, datasets)
```

### Custom Validation Rules

```python
# Add custom validation rules
validator = NYTDDataValidator("297")

# Custom rule: Employment consistency
def validate_employment_consistency(df):
    issues = []
    # Full-time and part-time employment should be mutually exclusive
    both_employed = df[(df['CurrFTE'] == 1) & (df['CurrPTE'] == 1)]
    if len(both_employed) > 0:
        issues.append({
            'rule': 'Employment exclusivity',
            'count': len(both_employed),
            'description': 'Youth cannot be both full-time and part-time employed'
        })
    return issues

# Add to validator
validator.custom_validators = [validate_employment_consistency]
```

### Analysis-Ready Export

```python
from nytd_dataset_config import export_analysis_ready_dataset, calculate_dataset_readiness_score

# Calculate readiness score
readiness_score = calculate_dataset_readiness_score(df_cleaned, "297")
print(f"Analysis Readiness: {readiness_score['total']:.1f}/100")

# Export analysis-ready version
analysis_path = export_analysis_ready_dataset(
    df_cleaned, 
    "297", 
    "s3://bdc-public-curated/ndacan/nytd/outcomes/analysis_ready/"
)
```

---

## Best Practices

### 1. **Processing Workflow**
1. **Load and Inspect**: Always start with structure validation
2. **Validate Types**: Convert and validate data types before range checking
3. **Check Consistency**: Logical relationships after individual variable validation
4. **Apply Corrections**: Standardized corrections before quality assessment
5. **Document Everything**: Comprehensive logging and reporting

### 2. **Quality Assurance**
- **Threshold Monitoring**: Set quality score thresholds for automated alerts
- **Trend Analysis**: Monitor quality across cohorts and time
- **Validation Logs**: Maintain detailed logs of all corrections and decisions
- **Peer Review**: Cross-validate findings with domain experts

### 3. **Documentation Standards**
- **Process Documentation**: Jupyter notebooks with full processing details
- **Data Dictionaries**: Comprehensive variable documentation
- **Quality Reports**: Standardized quality assessment reports
- **Version Control**: Track all changes and processing versions

### 4. **Error Handling**
- **Graceful Degradation**: Continue processing with warnings for non-critical issues
- **Detailed Logging**: Capture all errors, warnings, and corrections
- **Recovery Procedures**: Clear steps for handling processing failures
- **Manual Review Flags**: Identify cases requiring human intervention

---

## Troubleshooting

### Common Issues and Solutions

#### **Issue: High Missing Data Rate (>30%)**
```python
# Diagnosis
missing_analysis = validator.analyze_missing_values(df)
high_missing_vars = [var for var, analysis in missing_analysis.items() 
                    if analysis['percentage'] > 30]

# Solutions
1. Check for systematic survey non-response (OutcmRpt != 1)
2. Verify data loading and parsing
3. Review cohort-specific data collection procedures
4. Consider multiple imputation for critical variables
```

#### **Issue: Value Range Violations**
```python
# Diagnosis
value_issues = validator.validate_value_ranges(df)
for issue in value_issues['invalid_values']:
    print(f"{issue['column']}: {issue['invalid_values']}")

# Solutions
1. Check for data entry errors (typos, extra digits)
2. Verify codebook version alignment
3. Review data export/import procedures
4. Apply range corrections with documentation
```

#### **Issue: Logical Consistency Failures**
```python
# Diagnosis
logical_issues = validator.validate_logical_consistency(df)
for issue in logical_issues:
    print(f"{issue['rule']}: {issue['count']} cases")

# Solutions
1. Review survey logic and skip patterns
2. Check for data processing errors
3. Verify temporal sequence of data collection
4. Document exceptions and create flags
```

#### **Issue: Cross-Dataset Inconsistencies**
```python
# Diagnosis
comparison_report = create_cross_dataset_validation_report(dfs, datasets)
for var, stats in comparison_report['variable_consistency'].items():
    missing_rates = [s['missing_rate'] for s in stats.values()]
    if max(missing_rates) - min(missing_rates) > 20:
        print(f"{var}: Inconsistent missing rates across datasets")

# Solutions
1. Standardize data collection procedures
2. Review cohort-specific survey implementations
3. Apply consistent cleaning rules across datasets
4. Document and flag dataset-specific differences
```

---

## Performance Optimization

### Large Dataset Handling
```python
# For datasets >100k records
import dask.dataframe as dd

# Use chunked processing
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    chunk_cleaned = validator.validate_data_types(chunk)
    # Process chunk...
```

### Parallel Processing
```python
from multiprocessing import Pool
import functools

# Process multiple datasets in parallel
def process_single_dataset(dataset_info):
    dataset_num, file_path = dataset_info
    return process_nytd_dataset(dataset_num, file_path)

# Run in parallel
dataset_list = [('202', 'file202.csv'), ('228', 'file228.csv'), 
                ('266', 'file266.csv'), ('297', 'file297.csv')]

with Pool(processes=4) as pool:
    results = pool.map(process_single_dataset, dataset_list)
```

### Memory Optimization
```python
# Use efficient data types
df_optimized = validator.optimize_memory_usage(df)

# Drop intermediate columns
df_cleaned = df_cleaned.drop(columns=['temp_var1', 'temp_var2'])

# Use categorical for repeated strings
df['St'] = df['St'].astype('category')
```

---

## API Reference

### Core Functions

#### `process_nytd_dataset(dataset_number, file_path)`
**Main processing function for single dataset**

**Parameters:**
- `dataset_number` (str): NYTD dataset identifier ('202', '228', '266', '297')
- `file_path` (str): Path to data file in S3

**Returns:**
- `tuple`: (cleaned_dataframe, validation_results_dict)

**Example:**
```python
df_clean, results = process_nytd_dataset("297", "nytd_outcomes_297.csv")
```

#### `create_dataset_specific_validator(dataset_number)`
**Factory function for dataset-specific validator**

**Parameters:**
- `dataset_number` (str): NYTD dataset identifier

**Returns:**
- `NYTDDataValidator`: Configured validator instance

#### `standardize_across_datasets(df_list, dataset_numbers)`
**Standardize variables across multiple datasets**

**Parameters:**
- `df_list` (List[pd.DataFrame]): List of cleaned dataframes
- `dataset_numbers` (List[str]): Corresponding dataset identifiers

**Returns:**
- `List[pd.DataFrame]`: Standardized dataframes

### Configuration Classes

#### `NYTDDatasetConfig`
**Static configuration class for dataset specifications**

**Key Methods:**
- `get_dataset_info(dataset_number)`: Dataset metadata
- `get_expected_columns(dataset_number)`: Expected column list
- `get_wave_specific_rules(dataset_number)`: Wave validation rules

#### `NYTDDataValidator`
**Main validation engine**

**Key Attributes:**
- `validation_rules`: Dictionary of variable validation rules
- `expected_dtypes`: Expected data types for each variable
- `validation_results`: Comprehensive results of validation process

---

## Changelog

### Version 1.0.0 (2024-12-25)
- **Initial Release**: Complete validation framework for NYTD datasets 202, 228, 266, 297
- **Core Features**: Structure validation, type conversion, range checking, consistency validation
- **Quality Scoring**: Multi-dimensional quality assessment with analysis readiness scoring
- **Cross-Dataset**: Standardization and comparison across cohorts
- **Documentation**: Comprehensive user guide and API documentation
- **Export Features**: Analysis-ready datasets with data dictionaries

### Planned Enhancements (Version 1.1.0)
- **Machine Learning**: Predictive imputation models for missing values
- **Real-time Monitoring**: Automated quality alerts and dashboards
- **Advanced Analytics**: Built-in outcome analysis and visualization
- **API Integration**: REST API for external system integration

---

## Support and Contact

### Technical Support
- **Primary Contact**: Belmont Data Collaborative
- **Documentation**: This README and associated Jupyter notebooks
- **Code Repository**: SharePoint/BelmontDataCollaborative/NYTD_Processing/

### Data Questions
- **NYTD Specifications**: Refer to official NYTD Codebook and User's Guide
- **Dataset Issues**: Contact NDACAN (ndacan@cornell.edu)
- **Processing Questions**: Belmont Data Collaborative team

### Contributing
This framework follows an AI-first development approach. Contributions should:
1. **Maintain Quality**: All code must include comprehensive validation and error handling
2. **Document Thoroughly**: Include detailed docstrings and usage examples
3. **Test Extensively**: Validate against all supported datasets
4. **Follow Standards**: Adhere to established coding and documentation standards

---

## License and Acknowledgments

### Data Sources
- **NYTD Data**: National Data Archive on Child Abuse and Neglect (NDACAN)
- **Specifications**: NYTD Codebook and User's Guide from Children's Bureau, ACF, HHS

### Acknowledgments
- **Children's Bureau**: Administration on Children, Youth and Families, U.S. Department of Health & Human Services
- **NDACAN**: National Data Archive on Child Abuse and Neglect, Cornell University
- **Belmont University**: Data Collaborative team for framework development

### Citation
When using this framework or processed datasets, please cite:
```
Belmont Data Collaborative (2024). NYTD Data Validation and Cleaning Framework. 
Belmont University. https://github.com/belmont-data-collaborative/nytd-validation
```

---

**Last Updated**: December 25, 2024  
**Framework Version**: 1.0.0  
**Documentation Version**: 1.0.0 