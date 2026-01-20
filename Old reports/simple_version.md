<link rel="stylesheet" href="simple_version.css">

<div align="center">
<h1 class="report-title">NYTD Modeling: Visual Data Report</h1>
<h2 class="report-subtitle">A Statistical Analysis of Foster Care Youth Outcomes in Tennessee</h2>
</div>

<div class="navigation-and-toc-container">
    <div class="table-of-contents" id ="table-of-contents">
        <h2>📑 Table of Contents</h2>
        <ol>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#executive-summary">Executive Summary</a></li>
            <li><a href="#summary-dashboard">Summary Dashboard</a></li>
            <li><a href="#key-findings">Key Findings</a></li>
            <li><a href="#data-overview">Data Overview</a></li>
            <li><a href="#outcome-statistics">Outcome Statistics</a></li>
            <li><a href="#appendix-variable-definitions">Appendix: Variable Definitions</a></li>
            <li><a href="#appendix-all-tables">Appendix: All Tables</a></li>
            <li><a href="#appendix-charts-and-visualizations">Appendix: Charts and Visualizations</a></li>
        </ol>
    </div> 
    <div class="navigation-note">
        <h2>📋 How to Use This Report</h2>
        <ul>
            <li>Click on any section in the <strong>Table of Contents</strong> to jump directly to that analysis</li>
            <li>Each section contains <strong>Key Findings</strong> highlighted in boxes for easy scanning</li>
            <li>All charts and detailed data are in the <strong>Appendix</strong></li>
            <li>Statistical details support each finding</li>
        </ul>
    </div>
</div>

<div class="page-break"></div>

<div class="introduction" id="introduction">
<h1>Introduction</h1>

## 📊 Quick Facts
- **599 foster care youth** from Tennessee analyzed  
- **19 reliable relationships** found between care experiences and adult outcomes
- **3 cohorts** tracked from 2014-2024
- **6 key life areas** measured 1-4 years after leaving care

---

<p>This report analyzes outcomes for youth in foster care using Tennessee's National Youth in Transition Data (NYTD). The analysis identifies which factors during foster care predict success or challenges in young adulthood.</p>

**What We Studied:**
- Youth outcomes in education, housing, employment, and criminal justice
- Factors that influence these outcomes (placement type, services, demographics)
- Statistical relationships between experiences in care and adult results

**Data Sources:**
- NYTD Outcome Survey (ages 17, 19, 21)
- NYTD Services records 
- AFCARS placement data

**Key Limitations:**
- Small sample size (599 youth)
- Tennessee-specific results
- Voluntary participation creates bias
- Missing data from 2011 cohort
</div>

<div class="page-break"></div>

<div class="executive-summary" id="executive-summary">
<h1>Executive Summary</h1>

## 📋 Bottom Line Up Front
**19 reliable connections** found between foster care experiences and adult outcomes. **Placement stability** is the most important factor affecting youth success.

---

<div class="key-findings-box">
<h3>🎯 Most Important Findings</h3>

**Critical Risk Factors:**
- **Placement moves** - More moves = worse outcomes in all areas
- **Group home placement** - Higher incarceration rates than foster homes  
- **Male gender** - 5x more likely to be incarcerated
- **Having a disability** - Higher homelessness and lower employment

**Protective Factors:**
- **Stable placements** - Fewer moves lead to better outcomes
- **Foster homes** - Better results than group homes
- **Longer time in care** - Reduces some risks
- **Early adult relationships** - Strong lasting positive effects
</div>

## Key Statistics

**Challenges:**
- **35.7%** experienced incarceration  
- **29.3%** experienced homelessness
- **18.5%** received substance abuse referrals

**Successes:**
- **94.3%** maintain adult connections
- **64.8%** in education or employment
- **Foster homes** consistently outperform other placements

## What This Means
Keep youth in stable foster home placements with supportive adults. Focus extra resources on males, youth with disabilities, and those in group homes.
</div>

<div class="page-break"></div>

<div class="summary-dashboard" id="summary-dashboard">
<h1>📊 Summary Dashboard</h1>

---

<div class="dashboard-grid">
    <div class="dashboard-column">
        <h3>⚠️ Highest Risk Factors</h3>
        <table class="dashboard-table">
            <thead>
                <tr>
                    <th>Risk Factor</th>
                    <th>Impact</th>
                    <th>Affected Outcomes</th>           
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Placement Moves</strong></td>
                    <td>More moves = higher incarceration, homelessness, substance abuse</td>
                    <td>Criminal justice, housing, substance use, education</td>
                </tr>
                <tr>
                    <td><strong>Group Home Placement</strong></td>
                    <td>2x higher incarceration risk</td>
                    <td>Criminal justice involvement</td>
                </tr>
                <tr>
                    <td><strong>Having a Disability</strong></td>
                    <td>Higher homelessness, lower employment</td>
                    <td>Housing stability, education/employment</td>
                </tr>
                <tr>
                    <td><strong>Male Gender</strong></td>
                    <td>5x more likely to be incarcerated</td>
                    <td>Criminal justice involvement</td>
                </tr>
            </tbody>
        </table>
    </div>   
    <div class="dashboard-column">
        <h3>✅ Protective Factors</h3>
        <table class="dashboard-table">
            <thead>
                <tr>
                    <th>Protective Factor</th>
                    <th>Impact</th>
                    <th>Affected Outcomes</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Adult Relationships</strong></td>
                    <td>94.3% maintain supportive adults</td>
                    <td>Social connections</td>
                </tr>
                <tr>
                    <td><strong>Foster Home Placement</strong></td>
                    <td>Better outcomes than all other placements</td>
                    <td>Multiple positive outcomes</td>
                </tr>
                <tr>
                    <td><strong>Longer Time in Care</strong></td>
                    <td>Lower incarceration, better outcomes</td>
                    <td>Criminal justice, education/employment</td>
                </tr>
                <tr>
                    <td><strong>Service Access</strong></td>
                    <td>More education aid, higher enrollment</td>
                    <td>Educational outcomes</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="dashboard-stats-row">
    <div class="dashboard-stat">
        <span class="stat-number">1 in 3</span>
        <span class="stat-label">youth incarcerated</span>
    </div>
    <div class="dashboard-stat">
        <span class="stat-number">1 in 3</span>
        <span class="stat-label">youth homeless</span>
    </div>
    <div class="dashboard-stat">
        <span class="stat-number">94%</span>
        <span class="stat-label">keep adult connections</span>
    </div>
    <div class="dashboard-stat">
        <span class="stat-number">65%</span>
        <span class="stat-label">in school/working</span>
    </div>
</div>
</div>

<div class="page-break"></div>

<div class="key-findings" id="key-findings">
<h1>🔍 Key Findings</h1>

## 📈 Statistical Results Summary
**19 reliable relationships** found between foster care experiences and outcomes (p < 0.05).

---

### Most Important Predictors

**1. Placement Stability**
- Affects 4 different outcomes  
- More moves = higher incarceration (13.9x higher odds)
- More moves = higher substance abuse (12.2x higher odds)
- More moves = higher homelessness (4.4x higher odds)

**2. Gender Differences**  
- Males much more likely to be incarcerated
- Most reliable predictor in the analysis (99.99% confidence)

**3. Disability Status**
- Increases homelessness risk
- Decreases education/employment success
- Affects multiple life domains

**4. Placement Type**
- Group homes have higher incarceration rates
- Foster homes show better outcomes across measures

### Outcome-Specific Findings

**🏠 Education & Employment Success:**
- **Stable placements** help
- **Females** do better  
- **Longer time in care** helps
- **Having a disability** hurts

**⚖️ Criminal Justice Involvement:**
- **Males** at much higher risk
- **Group homes** increase risk
- **More placement moves** increase risk  
- **Longer time in care** reduces risk

**🏘️ Housing Stability:**
- **Having a disability** increases homelessness
- **More placement moves** increase homelessness

**💊 Substance Use:**
- **More placement moves** increase referrals
- **Longer time in care** slightly reduces risk

**🤝 Adult Connections:**
- **Early supportive relationships** predict lasting connections
- **94.3%** of youth maintain these relationships

<div class="key-insight">
<h3>💡 Key Insight</h3>
<p><strong>Placement stability emerges as the most universal predictor.</strong> Youth with frequent placement moves struggle across nearly every outcome measured. This suggests that reducing placement disruptions should be a top policy priority.</p>
</div>
</div>

<div class="page-break"></div>

<div class="data-overview" id="data-overview">
<h1>📋 Data Overview</h1>

### Primary Data Sources
- **NYTD Outcome Survey:** Youth outcomes at ages 17, 19, and 21
- **NYTD Services:** Service utilization records  
- **AFCARS:** Placement history and demographics
- **Final Dataset:** 599 youth with complete data

### Analysis Approach
- **Method:** Statistical analysis (logistic regression)
- **Focus:** Reliable relationships between experiences and outcomes
- **Significance Level:** p < 0.05 for reliable findings
- **Validation:** Manual checks and cross-validation of results

### Data Quality
- **Missing Data:** Very low (under 2% for most outcomes)
- **Sample Size:** 599 youth from 3 cohorts (2014-2024)  
- **Geographic Scope:** Tennessee only
- **Participation:** Voluntary (introduces selection bias)
</div>

<div class="page-break"></div>

<div class="outcome-statistics" id="outcome-statistics">
<h1>📊 Outcome Statistics</h1>

## 📋 Results by Life Domain

### 🏠 Housing & Family
| Outcome | Rate | Count | Interpretation |
|---------|------|-------|----------------|
| **Having Children (Unmarried)** | 22.4% | 159/709 | About 1 in 5 youth |
| **Experiencing Homelessness** | 29.3% | 211/719 | Nearly 1 in 3 youth |

### 🎓 Education & Employment  
| Outcome | Rate | Count | Interpretation |
|---------|------|-------|----------------|
| **Education/Employment** | 64.8% | 464/716 | Nearly 2 out of 3 youth |
| **Adult Connections** | 94.3% | 678/719 | Almost all youth |

### ⚖️ Criminal Justice & Health
| Outcome | Rate | Count | Interpretation |
|---------|------|-------|----------------|
| **Incarceration** | 35.7% | 256/718 | About 1 in 3 youth |
| **Substance Abuse Referrals** | 18.5% | 133/717 | About 1 in 6 youth |

<div class="key-insight">
<h3>📈 Key Insights</h3>
<ul>
<li><strong>Most youth maintain adult connections</strong> (94.3%) - major success</li>
<li><strong>Two-thirds pursue education/employment</strong> (64.8%) - positive trend</li>  
<li><strong>One in three face major challenges</strong> (incarceration/homelessness) - areas for improvement</li>
<li><strong>Data quality is excellent</strong> - missing data under 2%</li>
</ul>
</div>
</div>

<div class="page-break"></div>

<div align="center">
<h1 class="report-title">Appendix</h1>
<h2 class="report-subtitle">Detailed Data, Charts, and Model Results</h2>
</div>

<div class="appendix-variable-definitions" id="appendix-variable-definitions">
<h1>📋 Variable Definitions</h1>

<blockquote>
<p><strong>📋 Reference:</strong> These variables support findings in <a href="#key-findings">Key Findings</a>, <a href="#outcome-statistics">Outcome Statistics</a>, and <a href="#summary-dashboard">Summary Dashboard</a>.</p>
</blockquote>

### Outcome Variables (What We Measured)
| Domain | Variable | Description |
|--------|----------|-------------|
| **Education & Employment** | Connected_Youth | In school or working full-time |
| **Social Connections** | CnctAdult_w23 | Has supportive adult relationship |
| **Housing** | Homeless_w23 | Experienced homelessness |
| **Health & Wellness** | SubAbuse_w23 | Received substance abuse referral |
| **Criminal Justice** | Incarc_w23 | Was incarcerated |
| **Family** | Children_NoMarriage_w23 | Had children without marriage |

### Predictor Variables (What We Studied)
| Domain | Variable | Description |
|--------|----------|-------------|
| **Demographics** | Sex | Male or female |
| **Disability Status** | DiagDis | Diagnosed with a disability |
| **Placement Factors** | PlacementType | Where placed (foster home, group home, other) |
| **Placement Factors** | PlacementInstability | Number of different placements |
| **Placement Factors** | MonthsInCare | Total time in foster care system |
| **Early Indicators** | SubAbuse_w1 | Substance abuse referral while in care |
| **Early Indicators** | CnctAdult_w1 | Had supportive adult while in care |
| **Removal Reasons** | RR_neglect, RR_abuse, RR_other | Why removed from home |
</div>

<div class="page-break"></div>

<div class="appendix-tables" id="appendix-all-tables">
<h1>📊 Complete Statistical Results</h1>

<blockquote>
<p><strong>📋 Reference:</strong> These tables provide complete statistical support for <a href="#key-findings">Key Findings</a> and <a href="#summary-dashboard">Summary Dashboard</a>.</p>
</blockquote>

### Top 10 Most Reliable Findings
| Rank | Finding | Confidence | Effect Size | Impact |
|------|---------|------------|-------------|---------|
| 1 | Males more likely incarcerated | 99.99% | Large | Major risk factor |
| 2 | Group homes increase incarceration | 99.99% | Large | Placement matters |
| 3 | Other placements increase incarceration | 99.93% | Large | Foster homes best |
| 4 | More moves increase incarceration | 99.89% | Very Large | Stability crucial |
| 5 | Longer care reduces incarceration | 99.85% | Medium | Time helps |
| 6 | More moves increase substance abuse | 98.92% | Very Large | Multiple impacts |
| 7 | Disabilities increase homelessness | 98.84% | Medium | Support needed |
| 8 | More moves reduce education success | 99.18% | Large | Affects everything |
| 9 | Adult connections predict connections | 96.76% | Large | Relationships matter |
| 10 | Disabilities reduce education success | 97.72% | Medium | Barrier to success |

### Outcome Frequency Summary
| Outcome | Yes | No | Total | Success Rate |
|---------|-----|----|----|--------------|
| Adult Connections | 678 | 41 | 719 | 94.3% |
| Education/Employment | 464 | 252 | 716 | 64.8% |
| Incarceration | 256 | 462 | 718 | 35.7% (challenge) |
| Homelessness | 211 | 508 | 719 | 29.3% (challenge) |
| Children (Unmarried) | 159 | 550 | 709 | 22.4% |
| Substance Abuse | 133 | 584 | 717 | 18.5% (challenge) |
</div>

<div class="page-break"></div>

<div class="appendix-charts" id="appendix-charts-and-visualizations">
<h1>📈 Charts and Visualizations</h1>

<blockquote>
<p><strong>📋 Reference:</strong> These visualizations support findings in <a href="#outcome-statistics">Outcome Statistics</a>, <a href="#key-findings">Key Findings</a>, and <a href="#summary-dashboard">Summary Dashboard</a>.</p>
</blockquote>

### Available Charts
- **Forest Plots by Outcome** - Shows effect sizes for all reliable findings
- **Outcome Distribution Bar Charts** - Visual breakdown of all outcome rates  
- **Predictor Distribution Bar Charts** - Shows distribution of risk factors
- **Placement and Care Distribution** - Time in care and placement patterns
- **Variable Frequency Plot** - Which factors appear most often in results
- **Model Results Dashboard** - Statistical summary ranked by effect size

*Note: Chart images referenced in original document (all_visual_data_forest_plot.png, each_outcome_bar_chart.png, etc.) provide detailed visual representation of these findings.*
</div>

<div class="page-break"></div>

<div class="appendix-section" id="source-files">
<h1>📋 Methods and References</h1>

<blockquote>
<p><strong>📋 Reference:</strong> Complete methodology supports analysis in <a href="#key-findings">Key Findings</a> and statistical approach.</p>
</blockquote>

### Analysis Method
- **Statistical Approach:** Logistic regression for binary outcomes
- **Significance Level:** p < 0.05 for reliable findings  
- **Sample Size:** 599 youth with complete data
- **Validation:** Manual verification of key results

### Data Sources
- **Foster Care Analysis Reports:** univariate_analysis_report_v3.pdf, bivariate_analysis_report_v4.pdf
- **Model Creation:** all_visual_data.ipynb
- **Research Foundation:** "Aging Out of Foster Care: Homelessness, Post-Secondary Education, and Employment" (Journal of Public Child Welfare)

### Key Limitations
- **Geographic Scope:** Tennessee only - results may not apply elsewhere
- **Sample Size:** Relatively small for some subgroup analyses  
- **Selection Bias:** Voluntary participation affects generalizability
- **Missing Data:** 2011 cohort could not be included due to ID matching issues

### Data Quality Notes
- **NYTD Outcomes:** 720 youth across 4 cohorts (2011-2024)
- **AFCARS Match:** 599 youth across 3 cohorts (2014-2024)
- **Missing Data Rate:** Under 2% for most key variables
- **Validation:** Cross-checked unique identifiers and calculations
</div>

<a href="#table-of-contents">Return to Table of Contents</a>