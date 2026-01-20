# **Report Development Documentation – Pre-Model Phase**
**From Initial Dataset Creation to report_style.pdf**

---

## **1. Purpose**
Before the statistical modeling in `multi_model.ipynb` began, an extensive **data preparation and descriptive reporting phase** was completed.  
This phase produced the **`report_style.pdf`**, a pre/post outcome comparison report for Tennessee foster care youth, which served as the foundation for later modeling and the `all_visual_data_report.pdf`.

---

## **2. Data Acquisition**
### **Primary Source**
- **National Data Archive on Child Abuse and Neglect (NDACAN)** – NYTD Outcomes and Services data for Tennessee.
- Data was collected for **four longitudinal cohorts** surveyed at three points in time:
  - **Wave 1** (age 17) – In care  
  - **Wave 2** (age 19) – Post-transition  
  - **Wave 3** (age 21) – Post-transition  

### **Cohort Years**
- 2011–2015  
- 2014–2018  
- 2017–2021  
- 2020–2024  

---

## **3. Data Preparation & Integration**
### **Step 1 – Cohort Merging**
- All four cohorts were combined into a **single master dataset**.
- Youth were **filtered** to include only Tennessee foster care participants.
- **Duplicates removed** based on unique participant IDs.

### **Step 2 – Wave Consolidation**
- The goal was to compare **baseline in-care data (Wave 1)** to **post-transition data (Waves 2 & 3)**.
- Post-transition consolidation logic:
  - If “yes” in **either** wave 2 or 3 → final value = “yes”.
  - If “no” in both waves → final value = “no”.
  - If missing in one wave but available in the other → use available response.

### **Step 3 – Binary Variable Structure**
- Responses transformed to **binary format** (`1` = yes, `0` = no).
- Example outputs:
  - `all_binary_counts_merged.csv` – binary indicators for all outcomes by wave.
  - `combined_w1_w23_binary_counts.csv` – merged binary results for pre/post analysis.

---

## **4. Outcome Measurement**
### **Key Outcome Domains** (21 total variables)
- **Housing Stability** (e.g., Homelessness, Public Housing Assistance)
- **Employment** (e.g., Full-time/Part-time Employment, Job Training)
- **Financial Independence** (e.g., Food Assistance, Social Security Benefits)
- **Education & Training** (e.g., GED attainment, Higher Education)
- **Family & Children** (e.g., Has Children, Married at Child’s Birth)
- **Adult Support** (e.g., Supportive Adult Connection)
- **Justice System Involvement** (e.g., Ever Incarcerated)

### **Metrics Calculated**
For each outcome:
1. **Wave 1 Percentage** – Baseline prevalence at age 17.
2. **Waves 2 & 3 Combined Percentage** – Post-transition prevalence.
3. **Combined Lifetime Percentage** – Any occurrence across all waves.

---

## **5. Analysis Approach**
- **Descriptive change analysis**: Compare baseline to post-transition to highlight shifts in prevalence.
- Focus on:
  - **Increase in challenges** (e.g., homelessness, food assistance reliance).
  - **Positive progress** (e.g., employment, skill training).
  - **Stable protective factors** (e.g., adult connections).
- Calculations based on cleaned, deduplicated binary dataset.

---

## **6. Report Creation – `report_style.md`**
### **Structure**
- **Executive Summary** – Key insights and “at a glance” table.
- **Methods** – Data source, cohort structure, and integration process.
- **Outcome Sections** – Each domain with:
  - Definition of what the outcome measures.
  - Baseline, post-transition, and combined results in tables.
  - Narrative interpretation of findings.
- **Appendix** – Variable definitions and diagrams.

### **Design Features**
- Written in **Markdown** with embedded HTML for table formatting.
- Used **CSS styling** for visual consistency.
- Included **navigation links** (“Back to Table”) and in-text anchors.
- Added **icons and color highlights** for visual engagement.

---

## **7. PDF Generation – `report_style.pdf`**
### **Conversion Process**
1. Convert `report_style.md` → HTML with CSS styling.
2. Export HTML → PDF using a tool that preserves:
   - **Clickable links**
   - **Table formatting**
   - **Page breaks** for each major section.
3. Validate PDF layout:
   - All sections start on a new page.
   - Visual elements align properly.
   - Links and appendices are functional.

---

## **8. Role in Later Modeling**
- The cleaned **binary outcome dataset** from this phase became the **input for multi_model.ipynb**.
- The descriptive analysis provided:
  - A **baseline** understanding of variable distributions.
  - Early **hypotheses** about predictors of outcomes.
- **Significant variables** identified in `all_visual_data_report.pdf` were built upon the dataset creation and logic established in `report_style.pdf`.

---

## **Summary Workflow (Pre-Model Phase)**
NDACAN NYTD Raw Data
↓
Cohort Filtering (Tennessee only)
↓
Wave Alignment & Merge
↓
Binary Transformation
↓
Pre/Post Outcome Calculations
↓
Descriptive Report Writing (report_style.md)
↓
PDF Export (report_style.pdf)
---
This pre-model stage ensured a **clean, analyzable dataset** and a **descriptive statistical foundation** before running logistic regression models in the later reporting phase.


# **Report Development Documentation-Model Phase**
**From multi_model.ipynb to all_visual_data_report.pdf**

---

## **1. Overview**
This documentation outlines the workflow for creating the *NYTD Modeling: Visual Data Report*, detailing each step from **model generation** in `multi_model.ipynb` to the final polished PDF, `all_visual_data_report.pdf`.

The process integrates:
- **Data preparation and model execution** in Jupyter notebooks.
- **Result validation** using verification scripts.
- **Markdown report assembly** with HTML/CSS styling.
- **Final PDF export** with layout and link preservation.

---

## **2. Data Sources and Inputs**
### **Primary Datasets**
- **NYTD Outcome Survey** – Longitudinal outcomes at ages 17, 19, 21.
- **NYTD Services** – Service utilization records before age 18.
- **AFCARS** – Case-level foster care administrative data.

**Merged Final Dataset:** `wave_service_afcars_final.csv`  
Contains 720 youth records; final modeling used **599** participants where AFCARS could be matched.

**Supporting Files**:
- `significant_model_results.csv` – Model coefficients and significance flags.
- `predictor_stats_detailed_df.csv` – Counts, percentages, and distributions for predictors.
- `outcome_stats_detailed_df.csv` – Counts, percentages, and distributions for outcomes.
- `comprehensive_clean_dataset.csv` – Cleaned and standardized base dataset.

---

## **3. Model Development – multi_model.ipynb**
### **Objective**
Identify statistically significant relationships between **predictor variables** (e.g., demographics, placement history, service access) and **post-transition outcomes** (e.g., education, incarceration, housing stability).

### **Model Creation Process**
1. **Data Preparation**
   - Load `wave_service_afcars_final.csv`.
   - Restrict dataset to **Tennessee foster care youth**.
   - Merge NYTD Outcomes, NYTD Services, and AFCARS using a unique personal ID and cohort year.
   - Standardize variable naming and formats.
   - Assign binary encoding (`1` = yes/experienced, `0` = no/did not experience, blank for missing/unknown).

2. **Feature Engineering**
   - **Placement Instability**: Count of placement moves, converted into categorical risk levels.
   - **Service Count**: Sum of all NYTD services received pre-transition (`services_amount` column).
   - Dummy encoding for categorical predictors such as `PlacementType` (e.g., Foster Home, Group Home, Other).
   - Cohort and demographic flags (e.g., sex, race/ethnicity).

3. **Outcome Definition**
   - Six binary outcome variables:
     - `Connected_Youth` (connected to education or employment)
     - `CnctAdult_w23` (maintain supportive adult connections)
     - `Homeless_w23`
     - `Incarc_w23`
     - `Children_NoMarriage_w23`
     - `SubAbuse_w23` (substance abuse referrals)

4. **Logistic Regression Modeling**
   - **Approach**: One model per outcome–predictor set.
   - **Method**: `statsmodels.Logit` used for logistic regression.
   - **Interpretation**:
     - Coefficients (log-odds) indicate effect direction and magnitude.
     - p-values test statistical significance (threshold **p < 0.05**).
     - Confidence intervals calculated for all coefficients.
   - **Controls**: Demographic covariates included to isolate predictor effects.

5. **Model Output Generation**
   - All model results saved to `all_model_results.csv`.
   - Significant results filtered into `significant_model_results.csv`.
   - Predictor and outcome descriptive stats saved into respective detailed CSVs.

---

## **4. Data Extraction for Reporting**
Once models were run, specific outputs were extracted for later integration into the report:

### **From significant_model_results.csv**
- List of all predictors with **p < 0.05**.
- Corresponding coefficients, p-values, and confidence intervals.
- Grouping of significant predictors by outcome.
- Identification of **strongest effects** (largest absolute coefficient values).
- Ranking of predictors by statistical certainty (lowest p-values).

### **From predictor_stats_detailed_df.csv**
- Frequency and percentage distribution of each predictor variable.
- Used to describe sample characteristics (e.g., % with disability, % placed in group homes).

### **From outcome_stats_detailed_df.csv**
- Counts and percentages for each outcome.
- Directly used in the dashboard section (e.g., 94.3% maintain adult connections, 64.8% in education/employment).

### **From descriptive statistics in multi_model.ipynb**
- Cohort breakdowns.
- Cross-tabulations for key variable combinations (e.g., sex by incarceration).
- Summary metrics for services and placements.

---

## **5. Verification – comprehensive_data_verification.md**
### **Purpose**
Cross-check every statistic reported in the final document against model outputs and descriptive stats.

### **Steps**
1. Load relevant CSV files into a verification notebook.
2. Recalculate:
   - Percentages for dashboard claims.
   - Number of significant results.
   - Largest coefficients and their corresponding predictors.
3. Flag discrepancies:
   - Example: `"5 times more likely to be incarcerated"` corrected to ~**1.3x**.
4. Approve only verified statistics for report inclusion.

---

## **6. Report Assembly – all_visual_data_report.md**
### **Structure**
Written in **Markdown** with embedded HTML for structure and linked `style.css` for styling.

**Sections:**
1. Introduction
2. Summary Dashboard
3. Executive Summary
4. Data Curation & Methodology
5. Data Overview
6. Significant Variables
7. Significant Model Results
8. Descriptive Statistics
9. Outcome Distributions
10. Variable Importance & Effect Sizes
11. Appendices (Variable Definitions, All Tables, Model Details, Charts, Data Breakdown, Source References)

### **Styling**
- `style.css` controls typography, color palette, and table styling.
- HTML `<div class="page-break">` tags inserted for PDF pagination.
- Internal navigation via "Return to Table of Contents" links.

---

## **7. Visualization Integration**
From **significant_visuals.ipynb**:
- Horizontal bar charts showing predictor importance by effect size.
- Distribution histograms for outcomes and predictors.
- Appendices compile all charts for reference.

Charts are embedded into the markdown using relative image paths so they render both in HTML and PDF.

---

## **8. PDF Generation**
### **Process**
1. Convert `all_visual_data_report.md` to HTML, applying `style.css`.
2. Use a converter (e.g., Pandoc, wkhtmltopdf) to export HTML → PDF while:
   - Preserving **page breaks**.
   - Maintaining **clickable navigation links**.
   - Ensuring tables are not split across pages.
3. Review PDF for formatting, completeness, and navigation.

---

## **9. Quality Control Before Release**
- Re-run verification (`comprehensive_data_verification.md`) to ensure all reported stats are still correct.
- Visual inspection for:
  - Correct section breaks.
  - No missing images or broken links.
  - Tables rendering correctly.
- Final sign-off after confirming both **statistical accuracy** and **visual presentation**.

---

## **10. Output Files**
- **Analysis Notebooks**: `multi_model.ipynb`, `significant_visuals.ipynb`.
- **Processed Data**: `significant_model_results.csv`, `predictor_stats_detailed_df.csv`, `outcome_stats_detailed_df.csv`.
- **Verification**: `comprehensive_data_verification.md`.
- **Report Draft**: `all_visual_data_report.md`.
- **Final Report**: `all_visual_data_report.pdf`.

---

## **11. Summary Workflow Diagram**
Data Acquisition → Data Cleaning & Merge → Modeling (multi_model.ipynb)
↓ ↓
Descriptive Stats (predictor/outcome) Significant Results CSV
↓ ↓
Verification (comprehensive_data_verification.md)
↓
Report Writing (all_visual_data_report.md + style.css)
↓
Visual Integration (charts & tables)
↓
PDF Export (all_visual_data_report.pdf)

---

This process ensures the **final PDF report** is **statistically accurate**, **visually consistent**, and **navigable**, representing the verified results of the NYTD foster care outcomes modeling.
