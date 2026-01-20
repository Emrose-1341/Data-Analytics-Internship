## 2025 Tennessee Vulnerability and Prevention Index (TN VPI)

This document provides a high-level overview of the TN VPI project, including the live-updatable project folder structure and a consolidated table of data sources used in the original 2023 TN VPI and the additions for the updated 2025 refresh.

---

### Project Folder Structure (keep updated as project evolves)

- `analysis_implementation.py`: Main analysis script implementing vulnerability scoring and geographic aggregation.
- `requirements.txt`: Python dependencies.
- `README.md`: Foster care youth analysis documentation.
- `README_2025_TN_VPI.md`: This document.
- `auto_results/`: Auto-generated analysis outputs.
  - `county_vulnerability_summary.csv`
  - `zip_vulnerability_summary.csv`
  - `youth_vulnerability_summary.csv`
  - `vulnerability_analysis_visualizations.png`
- `data/`: Raw and processed data assets.
  - `IL YOUTH DATASET FROM FY23-25.xlsx`
  - `outputLayer_0.csv`
  - `tn_county_region.xlsx`, `TN_Regions.csv`
  - `bdaic created tables/`
    - `df_youth.csv`, `df_assessment_questions.csv`, `df_cans.csv`, `df_risk_fixed.csv`, ...
    - `tl_2024_us_county/` TIGER/Line county shapefile (cpg, dbf, prj, shp, shx)
- `notebooks/`: Jupyter notebooks for exploration and processing.
  - `initial_analysis.ipynb`, `new_initial_analysis.ipynb`, `corrected_percents.ipynb`, ...
  - Mapping and joined geojson/csv files
- `dcs/`: Project documentation (approach, reports, folder dictionary).
  - `Analytic_Approach_Document.md`
  - `TN_Foster_Care_Youth_Landscape_Report.md`
  - `Data_Folder_Dictionary.md`

> Note: Update this list as files/folders are added, removed, or renamed.

---

### Data Sources and Refresh Availability

The table below summarizes the original 2023 TN VPI sources and the additional sources incorporated for 2025, along with whether refreshed data (2024/2025) is available. Add or update links and availability notes as they are confirmed.

| Source Category | Dataset / Indicator | Original Year(s) | Provider | Refresh Availability (2024/2025) | Notes / Link Placeholder |
|---|---|---|---|---|---|
| TN VPI (2023) | Child welfare assessments (CANS, LifeSkills) | FY23-25 | TN DCS | Yes (internal) | `data/IL YOUTH DATASET FROM FY23-25.xlsx` |
| TN VPI (2023) | County boundaries | 2024 | US Census TIGER/Line | Yes (annual) | `data/bdaic created tables/tl_2024_us_county/` |
| TN VPI (2023) | Population denominators by county | 2020/ACS annual | US Census/ACS | Yes (ACS yearly) | Add ACS table/code link |
| TN VPI (2023) | Poverty/household indicators | ACS 5-year | US Census/ACS | Yes (annual) | Add ACS table/code link |
| TN VPI (2023) | Education indicators (if used) | 2023 | TN DOE | To confirm | Placeholder |
| Additional TN | TBI Human Trafficking Hotline Tips/Calls | 2023 | TBI / Polaris | To confirm 2024/2025 | Add request/URL placeholder |
| Additional TN | Network Illicit Massage Businesses (IMBs) count by county | 2023 | The Network | To confirm 2024/2025 | Add request/URL placeholder |
| National | At-Risk Industries indicators (adult-entertainment, hospitality, etc.) | 2023 | BDAIC curated | To confirm updates | Add methodology link |
| National | Feeding America—Map the Meal Gap (Food insecurity) | 2022/2023 | Feeding America | 2024 released | Add URL: feedingamerica.org research portal |
| National | SNAP/WIC participation rates | 2023 | USDA | 2024 available | Add USDA link |
| National | Housing cost burden (30%+ income) | ACS 5-year | US Census/ACS | Yes (annual) | Add ACS table/code link |
| National | Unemployment rate | 2023 | BLS LAUS | 2024 available | Add BLS link |
| National | Substance use/mortality proxies (overdose death rate) | 2023 | CDC WONDER | 2024 provisional | Add CDC link |
| National | Behavioral health providers per capita | 2023 | HRSA | 2024 available | Add HRSA link |

> Add rows for any additional indicators included in the 2025 refresh. Replace placeholders with specific table IDs (e.g., ACS table codes), URLs, and data vintages as confirmed.

---

### Change Log (for this document)

- 2025-10-15: Initial version created with project structure snapshot and sources table scaffolding including TN additions (TBI Hotline, IMBs) and national sources (At-Risk Industries, Map the Meal Gap, etc.).

---

### Maintenance Notes

- Keep the folder structure section synchronized with the repository as notebooks, scripts, and outputs evolve.
- As refreshed data becomes available, update the "Refresh Availability" and "Notes/Link" columns with exact versions (year/vintage) and URLs.
- When new indicators are added, include the provider, geographic coverage, and any aggregation/normalization notes needed for comparability across years.

