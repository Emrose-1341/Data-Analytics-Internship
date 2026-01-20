# Data-Analytics-Internship

This repository captures the work from a data analytics internship / class project focused on analyzing outcomes for youth in foster care.  
The main branch exists primarily as a landing page, with the analysis work and reports organized into dedicated feature branches.

### Table of Contents 
- **[Branch Overview and Purpose](#branch-overview-and-purpose)** – What lives in `main`, `DCS`, and `NYPD`.  
- **[Context and Goals](#context-and-goals)** – How this work fits into a class/internship.  
- **[Skills Developed in This Project](#skills-developed-in-this-project)** – Key technical and analytical skills practiced.  
- **[Improvements for the Future](#improvements-for-the-future)** – Ideas if the project continues.  

### Branch Overview and Purpose

- **`main`**  
  - **Purpose**: High-level overview of the internship/class project and documentation of the repository structure.  
  - **What it contains**: This README and any top‑level meta documentation that explains how to navigate the project and what each branch is for.  
  - **How to use it**: Start here to understand the big picture, then switch to one of the analysis branches (`DCS` or `NYPD`) for detailed notebooks and reports.

- **`DCS` branch**  
  - **Purpose**: Data exploration and reporting for a foster care–related dataset (e.g., Tennessee DCS / TN foster care youth landscape and related initiatives).  
  - **Key contents**:  
    - `Code/` – Jupyter notebooks for data cleaning, checking data quality, calculating percentages, clustering, mapping, and performing initial and revised analyses.  
    - `Data Reports/` – Markdown and PDF reports such as analytic approach documentation, data folder dictionary, data summary report, and a “TN Foster Care Youth Landscape” report.  
    - `README_2025_TN_VPI.md` – Context and documentation specific to the 2025 TN VPI–related work.  
  - **How to use it**:  
    - Checkout the branch: `git checkout DCS`.  
    - Open notebooks under `Code/` in Jupyter or VS Code and run them cell‑by‑cell for reproducible analysis.  
    - Use the documents in `Data Reports/` to understand data definitions, methodology, and findings.  
    - **To see the main DCS report**: open `Data Reports/data_summary_report.pdf` on the `DCS` branch.

- **`NYPD` branch**  
  - **Purpose**: Modeling and visualization work for National Youth in Transition Database (NYTD)–style foster care data, focusing on predictors, outcomes, and key visualizations.  
  - **Key contents**:  
    - `Code/` – Jupyter notebooks for first‑pass analysis, building multiple models, outcome prediction, services analysis, and generating significant visualizations and summary dashboards.  
    - `Old reports/` – Earlier reports, markdown/PDF summaries, visual assets (PNGs, SVGs), and verification documents for checking data quality and model results.  
    - Top‑level reports (e.g., `all_visual_data_report.pdf`, `foster_care_visualizations.md`, and time‑stamped NYTD reports) that summarize findings from the analysis.  
  - **How to use it**:  
    - Checkout the branch: `git checkout NYPD`.  
    - Run notebooks in `Code/` to reproduce analyses and model fitting.  
    - Review `Old reports/` and the summary reports to understand how the analysis evolved over time.  
    - **To see the main NYPD report**: open `all_visual_data_report.pdf` on the `NYPD` branch.

### Context and Goals

- **Context**: This repository was created for a **Data Analytics Internship / class project** focused on real‑world, policy‑relevant data.  
- **Goals**:  
  - Practice the full analytics lifecycle: data intake, cleaning, exploratory analysis, modeling, visualization, and reporting.  
  - Communicate key findings to stakeholders through written reports and visual summaries.  
  - Learn to use Git branches to separate major lines of work while keeping a clean main branch for documentation.

### Skills Developed in This Project

- **Data wrangling and cleaning**  
  - Working with messy, real‑world datasets in Jupyter notebooks.  
  - Handling missing values, correcting data types, and validating data integrity with dedicated “data checks” notebooks.  
  - Restructuring data for percent calculations, clustering, and mapping.

- **Exploratory data analysis (EDA)**  
  - Creating summary tables and descriptive statistics for foster care and transition‑age youth.  
  - Exploring distributions and relationships between predictors (e.g., services, demographics) and outcomes.  
  - Using visualizations (bar charts, forest plots, dashboards) to surface key patterns.

- **Statistical modeling and predictive analytics**  
  - Building and comparing multiple models to predict outcomes for youth in foster care.  
  - Interpreting model coefficients and variable importance for policy‑relevant questions.  
  - Evaluating models and identifying which predictors matter most across different outcomes.

- **Data visualization and reporting**  
  - Turning analytical results into stakeholder‑friendly visualizations and written reports (Markdown and PDF).  
  - Designing summary dashboards and forest plots to communicate complex model results.  
  - Documenting analytic approaches, data dictionaries, and verification steps.

- **Reproducible analysis and version control**  
  - Structuring work in Jupyter notebooks so analyses can be rerun from raw data to final figures.  
  - Using Git branches (`main`, `DCS`, `NYPD`) to organize separate analytic tracks and preserve earlier reports.  
  - Writing project documentation for classmates, instructors, and future collaborators.

### Improvements for the Future

If this project were to continue, some improvements and extensions that would be valuable include:

- **Code organization and modularization**  
  - Refactor repeated notebook code (e.g., cleaning, plotting functions) into reusable Python modules.  
  - Add clear configuration files (e.g., for data paths and model settings) to reduce manual edits in notebooks.

- **Testing and validation**  
  - Introduce automated checks for data quality and model assumptions (unit tests or validation scripts).  
  - Formalize train/test splits, cross‑validation, and out‑of‑sample evaluation for all predictive models.

- **Documentation and onboarding**  
  - Expand README files in each branch with step‑by‑step “how to reproduce everything from scratch.”  
  - Add more narrative context about the data sources, limitations, and ethical considerations when working with youth data.

- **Automation and deployment**  
  - Create scripts or Makefiles to automate common workflows (data cleaning, model runs, report generation).  
  - Explore turning key outputs into an interactive dashboard (e.g., with Streamlit, Dash, or a BI tool) for non‑technical stakeholders.

- **Data and methods enhancements**  
  - Incorporate additional data sources that could improve predictions or add context (e.g., county‑ or region‑level indicators).  
  - Experiment with alternative modeling approaches (e.g., tree‑based ensembles, survival models, or causal inference techniques) where appropriate.
