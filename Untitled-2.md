# **Report Development Documentation – Basic Data and Dataset Creation**

---

## **1. Purpose**
The first stage was to take multiple years of raw NYTD data and transform it into a **clean, harmonized, and analyzable dataset**.  
This dataset would serve as the **foundation** for both:
- The initial **descriptive pre/post outcome analysis** (Report 1 / `report_style.pdf`), and
- The later **predictive logistic regression modeling** (Final report).

---

## **2. Data Sources**
### **Primary Source**
- **National Data Archive on Child Abuse and Neglect (NDACAN)**  
  Dataset: National Youth in Transition Database (NYTD) Outcomes and Services files for Tennessee.

### **Cohort & Wave Structure**
| Wave | Age | Description        | Timeframe per Cohort |
|------|-----|--------------------|----------------------|
| Wave 1 | 17 | Youth in care      | 2011, 2014, 2017, 2020 |
| Wave 2 | 19 | Post-transition    | 2013, 2016, 2019, 2022 |
| Wave 3 | 21 | Post-transition    | 2015, 2018, 2021, 2024 |

**Cohort Years:**
- 2011–2015
- 2014–2018
- 2017–2021
- 2020–2024

---

## **3. Files Produced in This Stage**
- `all_waves_merged.csv` – Merged raw NYTD Outcomes for all cohorts/waves.
- `all_binary_counts_merged.csv` – Binary-coded (yes/no) responses for each wave.
- `combined_w1_w23_binary_counts.csv` – Pre/post consolidated dataset (Wave 1 vs Waves 2 & 3 combined).

---

## **4. Data Processing Steps**
### **Step 1 – Data Import**
- Source files from NDACAN were imported into Pandas DataFrames.
- All datasets loaded with `dtype=str` to avoid auto-type errors.

### **Step 2 – Filtering**
- Keep **only Tennessee youth** (`StFIPS` = Tennessee code).
- Exclude youth not identified as foster care cases.
- Remove rows with no outcome data across all waves.

### **Step 3 – Harmonization**
- Align column names across years and cohorts.
- Match variable codes to a **master NYTD codebook**.
- Ensure consistent encoding (`1` = Yes, `0` = No, `NaN` = missing).

### **Step 4 – Merge**
- Merge Wave 1, Wave 2, and Wave 3 for each youth using `PersonalID` and `Cohort`.
- Append all cohorts together into `all_waves_merged.csv`.

### **Step 5 – Binary Conversion**
- Convert categorical NYTD outcome variables to binary:
  - Yes → 1
  - No → 0
  - Missing stays blank
- Save as `all_binary_counts_merged.csv`.

### **Step 6 – Wave 2 & 3 Consolidation**
- Combine Waves 2 & 3 into a **single “post-transition” variable** for each outcome:
  - If `yes` in either wave → combined = `yes`.
  - If `no` in both → combined = `no`.
  - If one missing, use the available value.
- Save as `combined_w1_w23_binary_counts.csv`.

---

## **5. Output of This Stage**
A **clean, binary-coded dataset** with:
- Baseline (Wave 1) outcomes.
- Post-transition outcomes (Waves 2 & 3 combined).
- Ready for descriptive statistical comparison.

---

# **Report Development Documentation – Pre-Model Phase: Report 1 (`report_style.pdf`)**

---

## **1. Purpose**
Use the cleaned dataset to produce a **comprehensive pre/post outcome analysis**.  
This report provided **baseline insight** before predictive modeling.

---

## **2. Data Used**
- Input: `combined_w1_w23_binary_counts.csv`
- Sample: 720 youth with valid Wave 1 and post-transition data.

---

## **3. Outcomes Analyzed**
21 variables across **7 domains**:
1. Housing Stability
2. Employment
3. Financial Independence
4. Education & Training
5. Family & Children
6. Adult Support
7. Justice System Involvement

For each outcome:
- **Wave 1 %**
- **Post-transition %**
- **Lifetime %** (yes in any wave)

---

## **4. Analysis Method**
- **Counts**: Number of youth answering “yes”.
- **Percentages**: `(count / total valid responses) * 100`.
- **Change Measurement**: Post-transition % – Wave 1 %.

---

## **5. Report Creation – `report_style.md`**
### **Structure**
- **Executive Summary** – Key insights and “Key Findings at a Glance”.
- **Methods** – Data acquisition, cohort structure, and processing logic.
- **Domain Sections** – Each domain had:
  - Description of measurement.
  - Table with pre/post/lifetime results.
  - Analysis interpretation (e.g., "Homelessness rose by 17.8%").
- **Appendix** – Variable definitions from NYTD codebook.

### **Design Features**
- Markdown with HTML for table formatting.
- CSS for styling (`style.css`).
- “Back to Table” links for navigation.

---

## **6. Output**
- **`report_style.pdf`** – First official descriptive NYTD report.
- Served as:
  - Baseline descriptive reference.
  - Input for hypothesis-building for later modeling.

---

# **Report Development Documentation – Model Phase (`multi_model.ipynb`)**

---

## **1. Purpose**
Identify **predictors** of post-transition outcomes using logistic regression.

---

## **2. Data Used**
- **Primary Dataset**: `wave_service_afcars_final.csv`
  - NYTD Outcomes + NYTD Services + AFCARS foster care placement history.
- **Supporting Files**:
  - `predictor_stats_detailed_df.csv`
  - `outcome_stats_detailed_df.csv`
  - `significant_model_results.csv`

---

## **3. Modeling Workflow**
### **Step 1 – Load & Clean**
- Remove missing or invalid entries.
- Convert all numeric predictors to integer or float.
- Create dummy variables for categorical predictors (`PlacementType`, `RaceEthnicity`).

### **Step 2 – Group Variables**
- Demographics
- Placement History
- Disability
- Services Received
- Baseline Outcomes

### **Step 3 – Define Outcomes**
Six binary outcomes modeled:
- `Connected_Youth`
- `CnctAdult_w23`
- `Homeless_w23`
- `Incarc_w23`
- `Children_NoMarriage_w23`
- `SubAbuse_w23`

### **Step 4 – Logistic Regression**
- **Tool**: `statsmodels.Logit`
- One model per outcome-predictor combination.
- Extract:
  - Coefficient (log-odds)
  - p-value
  - 95% confidence interval

### **Step 5 – Significance Filtering**
- Keep results where **p < 0.05**.
- Save to `significant_model_results.csv`.

---

## **4. Output**
- **19 significant predictor–outcome relationships**.
- Effect size ranking of predictors.
- Verification cross-check in `comprehensive_data_verification.md`.

---

# **Report Development Documentation – Final Report (`all_visual_data_report.pdf`)**

---

## **1. Purpose**
Integrate:
- Descriptive statistics (from pre-model phase).
- Logistic regression results (from model phase).
- Visualizations into a single **final report**.

---

## **2. Data & Inputs**
- Verified statistics from `comprehensive_data_verification.md`.
- Charts from `significant_visuals.ipynb`.
- Tables from:
  - `predictor_stats_detailed_df.csv`
  - `outcome_stats_detailed_df.csv`
  - `significant_model_results.csv`

---

## **3. Report Assembly – `all_visual_data_report.md`**
### **Sections**
1. Introduction & Executive Summary
2. Data Overview
3. Significant Variables
4. Model Results
5. Descriptive Stats
6. Outcome Distributions
7. Effect Size Visualizations
8. Appendices

### **Design**
- Linked `style.css`.
- Page breaks with `<div class="page-break">`.
- Clickable TOC links.

---

## **4. PDF Conversion**
- Markdown → HTML → PDF.
- Ensure:
  - Clickable links.
  - Table integrity.
  - Correct pagination.

---

## **5. Output**
- **`all_visual_data_report.pdf`** – Fully integrated descriptive + predictive analysis report.
- Final product for distribution.
