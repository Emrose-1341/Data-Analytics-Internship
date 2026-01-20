## NYPD Branch – Modeling + Visualization (NYTD-style)

This README documents the **`NYPD` branch** of a **Data Analytics Internship / class project**. This branch focuses on **modeling and visualization** for foster care / NYTD-style data, including predictor–outcome analysis and report-ready figures.

### Table of Contents

- **Quick Report** – Where to find the main deliverable PDF.  
- **What’s in this branch** – Key folders/files and what they do.  
- **How to reproduce the analysis** – Typical notebook workflow.  
- **Notes / Improvements** – What to improve if continuing.

### Quick Report (Main Deliverable)

- **If you just want the NYPD report**: open `all_visual_data_report.pdf` (in this branch).

### What’s in This Branch

- **`Code/`**: Jupyter notebooks for analysis, modeling, and visualization.
  - `first_data_analysis.ipynb` – Initial exploratory analysis.
  - `multi_model.ipynb` – Multi-model comparisons / experimentation.
  - `model_predictor_outcome.ipynb` – Predictor → outcome modeling and interpretation.
  - `services.ipynb` – Services-focused analysis.
  - `significant_visuals.ipynb` – Generation of key/significant plots for reporting.
  - `all_visual_data.ipynb` – Consolidated visuals / report figure generation.

- **Reports / write-ups**
  - `all_visual_data_report.pdf` – **Primary report output for this branch**.
  - `foster_care_visualizations.md` – Narrative write-up supporting visual outputs.
  - `nytd_report_20250717_162046.md` – Snapshot report from a specific run/time.

- **`Old reports/`**
  - Earlier versions of reports and supporting assets (PNGs/SVGs), plus verification notes.
  - Useful for seeing how the analysis evolved and for locating older figures.

### How to Reproduce the Analysis

1. **Checkout the branch**
   - `git checkout NYPD`
2. **Open the notebooks**
   - Use JupyterLab or VS Code.
   - Suggested order:
     - `Code/first_data_analysis.ipynb`
     - `Code/multi_model.ipynb` and/or `Code/model_predictor_outcome.ipynb`
     - `Code/significant_visuals.ipynb`
     - `Code/all_visual_data.ipynb` (to generate consolidated visuals / final outputs)
3. **View the report**
   - Open `all_visual_data_report.pdf`

### Notes / Improvements (If Continuing)

- **Reproducibility**: add an environment file (e.g., `requirements.txt` or `environment.yml`) and standardize data paths/config.  
- **Automation**: convert repeated notebook steps into scripts/modules to regenerate figures + reports in one run.  
- **Evaluation**: formalize cross-validation and out-of-sample metrics consistently across all models.  
- **Documentation**: add a short “data inputs expected” section (what files, where they live, required columns) once data locations are finalized.
