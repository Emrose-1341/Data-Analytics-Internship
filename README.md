## DCS Branch – Data Exploration + Reporting (TN Foster Care)

This README documents the **`DCS` branch** of a **Data Analytics Internship / class project**. This branch focuses on **data exploration, cleaning, and reporting** for Tennessee Department of Children's Services (DCS) foster care data, including landscape analysis, mapping, and comprehensive data reports.

### Table of Contents

- **Quick Report** – Where to find the main deliverable PDF.  
- **What's in this branch** – Key folders/files and what they do.  
- **How to reproduce the analysis** – Typical notebook workflow.  
- **Notes / Improvements** – What to improve if continuing.

### Quick Report (Main Deliverable)

- **If you just want the DCS report**: open `Data Reports/data_summary_report.pdf` (in this branch).

### What's in This Branch

- **`Code/`**: Jupyter notebooks for data exploration, cleaning, analysis, and visualization.
  - `initial_analysis.ipynb` – Initial exploratory data analysis.
  - `initial_analysis_TS.ipynb` – Time-series focused initial analysis.
  - `new_initial_analysis.ipynb` – Revised/updated initial analysis.
  - `data checks.ipynb` – Data quality checks and validation.
  - `Table_Data_type_altering.ipynb` – Data type corrections and transformations.
  - `Percents.ipynb` – Percentage calculations and aggregations.
  - `corrected_percents.ipynb` – Revised percentage calculations.
  - `region_corrected.ipynb` – Region-based corrections and analysis.
  - `Maping.ipynb` – Geographic mapping and visualization.
  - `Maping_percent.ipynb` – Mapping with percentage overlays.
  - `data_cluster_testin.ipynb` – Clustering analysis and testing.

- **`Data Reports/`**: Comprehensive reports and documentation.
  - `data_summary_report.pdf` – **Primary report output for this branch**.
  - `data_summary_report.md` – Markdown version of the summary report.
  - `TN_Foster_Care_Youth_Landscape_Report.pdf` – TN Foster Care Youth Landscape analysis report.
  - `TN_Foster_Care_Youth_Landscape_Report.md` – Markdown version of the landscape report.
  - `Analytic_Approach_Document.pdf` – Documentation of the analytical approach and methodology.
  - `Analytic_Approach_Document.md` – Markdown version of the approach document.
  - `Data_Folder_Dictionary.pdf` – Data dictionary and folder structure documentation.
  - `Data_Folder_Dictionary.md` – Markdown version of the data dictionary.

- **`README_2025_TN_VPI.md`**: Additional documentation specific to the 2025 Tennessee Vulnerability and Prevention Index (TN VPI) project, including project structure, data sources, and refresh availability.

### How to Reproduce the Analysis

1. **Checkout the branch**
   - `git checkout DCS`
2. **Open the notebooks**
   - Use JupyterLab or VS Code.
   - Suggested order:
     - `Code/data checks.ipynb` (start with data quality validation)
     - `Code/initial_analysis.ipynb` or `Code/new_initial_analysis.ipynb` (exploratory analysis)
     - `Code/Table_Data_type_altering.ipynb` (data cleaning and type corrections)
     - `Code/Percents.ipynb` or `Code/corrected_percents.ipynb` (percentage calculations)
     - `Code/region_corrected.ipynb` (region-based analysis)
     - `Code/Maping.ipynb` or `Code/Maping_percent.ipynb` (geographic visualizations)
     - `Code/data_cluster_testin.ipynb` (clustering analysis, if needed)
3. **View the reports**
   - Open `Data Reports/data_summary_report.pdf` for the main summary report.
   - Review other PDFs in `Data Reports/` for additional documentation and findings.

### Notes / Improvements (If Continuing)

- **Reproducibility**: add an environment file (e.g., `requirements.txt` or `environment.yml`) and document expected data file locations/names.  
- **Data organization**: create a clear `data/` folder structure with raw vs. processed data separation, and document data sources in a centralized location.  
- **Code modularization**: refactor repeated cleaning/transformation steps from notebooks into reusable Python modules or functions.  
- **Documentation**: expand the data dictionary with detailed column descriptions, data types, and any known data quality issues or limitations.  
- **Automation**: create scripts to automate the report generation pipeline (notebooks → markdown → PDF conversion) for easier updates when data refreshes.

