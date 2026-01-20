# 🏠 Youth Outcomes After Transitioning from Foster Care
## 📊 A Pre-Post Analysis of Tennessee Foster Care Youth


## 📋 Note on Navigating This Report

**This report is interactive:**
- 📈 In **Executive Summary**, click 'wave 1' or 'wave 2 & wave 3' to understand more about what they mean
- 🎯 Click on any finding in the **Key Findings at a Glance** section to jump directly to the detailed data table and analysis
- 📖 Within the data tables, click on any **Outcome** variable to view its definition in the appendix

---

## 📈 Executive Summary
---

This report analyzes **21 key outcomes** for Tennessee foster care youth, comparing their experiences while in care ([wave 1](#wave-variable-description)) to their outcomes after transitioning to adulthood ([waves 2 & 3](#wave-variable-description)), using data from the [National Youth in Transition Database (NYTD)](https://www.ndacan.acf.hhs.gov/datasets/dataset-details.cfm?ID=297).

<a name="wave-variable-description"></a>

### 📊 Overall Summary Findings:

> 🔍 **Key Insight:** After leaving foster care, youth face increased challenges with housing stability and economic security, including a significant rise in homelessness and greater reliance on public assistance.

> 💪 **Positive Outcomes:** Despite these challenges, there are notable improvements in employment and job training participation, and fewer youth become involved with the justice system after transition.

### 🎯 Key Findings at a Glance:

| Finding | Quick Summary |
|---------|---------------|
| 🏠 [Housing instability increases after foster care](#🏠-housing-stability) | Significant rise in homelessness |
| 💼 [Employment and job training participation rise substantially](#💼-employment) | Supporting economic self-sufficiency |
| 💵 [Reliance on public and financial assistance increases](#💵-financial-independence) | Highlighting ongoing economic vulnerability |
| 🎓 [Educational attainment remains stable](#🎓-education--training) | Continued support needed for progress |
| 👥 [Social connections and supportive relationships grow](#👥-social-connections--support) | Important protective factors |
| ⚖️ [Justice system involvement declines](#⚖️-justice-system-involvement) | Fewer youth incarcerated after foster care |

---
<div style="page-break-after: always;"></div>

---

# 🔬 <span style="background: #e3eafc; padding: 4px 12px; border-radius: 6px;">Methods</span>

---

## <span style="color: #2b7bb9;">📊 Dataset Acquisition</span>


**Primary Data Source:**  
<a href="https://www.ndacan.acf.hhs.gov/" target="_blank"><strong>National Data Archive on Child Abuse and Neglect (NDACAN)</strong></a>

<strong>Cohort Structure:</strong><br>
Four longitudinal cohorts of Tennessee foster care youth were followed at three time points:
<br><br>
<table>
  <tr>
    <th>Age</th>
    <th>Wave</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>📅 <strong>17</strong></td>
    <td>Wave 1</td>
    <td>In care</td>
  </tr>
  <tr>
    <td>📅 <strong>19</strong></td>
    <td>Wave 2</td>
    <td>Post-transition</td>
  </tr>
  <tr>
    <td>📅 <strong>21</strong></td>
    <td>Wave 3</td>
    <td>Post-transition</td>
  </tr>
</table>

<br>

<strong>Cohort Years:</strong><br>
<span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">2011–2015</span><br>
<span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">2014–2018</span><br>
<span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">2017–2021</span><br>
<span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">2020–2024</span>

---

## <span style="color: #2b7bb9;">🔧 Data Preparation & Integration</span>


**Sample Overview:**

| Wave | Youth Count |
|------|:----------:|
| 📈 **Wave 1** | <span style="color:#2b7bb9;"><strong>3,068</strong></span> |
| 📈 **Wave 2** | <span style="color:#2b7bb9;"><strong>1,362</strong></span> |
| 📈 **Wave 3** | <span style="color:#2b7bb9;"><strong>950</strong></span> |
| 📈 **Final Analytic Sample** | <span style="color:#2b7bb9;"><strong>720</strong></span> <span style="font-size: 0.95em;">(with valid data across relevant waves)</span> |

<br>

**Processing Steps:**
- All four cohorts were merged into a single dataset.
- Only youth identified as foster children in Tennessee were included.
- Data were de-duplicated and organized by unique participant ID.

<br>

**Wave Consolidation:**
- To represent post-transition outcomes, responses from waves 2 and 3 were combined for each participant:
    - <span style="color:#2b7bb9;">If a participant answered 'yes' in either wave 2 or wave 3, the combined value was set to 'yes'.</span>
    - <span style="color:#2b7bb9;">If a participant answered 'no' in both waves, the combined value was set to 'no'.</span>
    - <span style="color:#2b7bb9;">If data were missing for one wave but present for the other, the available response was used.</span>

</div>

---

## <span style="color: #2b7bb9;">📋 Outcome Measurement & Analysis</span>


- For each outcome, the count and percentage of 'yes' responses were calculated for:
    - <span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">**Baseline (Wave 1):** Youth in care at age 17</span>
    - <span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">**Post-Transition (Waves 2 & 3 Combined):** Youth after leaving care (ages 19 and/or 21)</span>
    - <span style="background: #e3eafc; padding: 2px 8px; border-radius: 4px;">**Combined:** Total unique 'yes' responses across all waves</span>
- Analyses focused on changes in outcome prevalence from baseline to post-transition, highlighting key shifts in youth experiences.

</div>

</div>
---

<div style="page-break-after: always;"></div>

---
# 📊 Key Outcomes: Before and After Transition
---

## 🏠 Housing Stability

> **What this domain measures:** This domain evaluates whether youth have secure, consistent, and safe living arrangements. On the baseline survey, youth responded "yes" if they had experienced these conditions at any point from age 0 to 17.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 🏚️ [**Experienced Homelessness**](#homeless-variable-description) | **11.5%** | **29.3%** | **36.8%** |
| 🏘️ [**Receiving Public Housing Assistance**](#public-housing-assistance-variable-description) | **1.7%** | **7.6%** | **7.9%** |

#### 📈 Analysis:
> **📊 Key Finding:** Overall, housing instability increases during post-transition.
> 
> - ⚠️ The rate of homelessness increases by **17.8%** after foster care

---
## 💼 Employment

> **What this domain measures:** This domain assesses the extent to which youth are engaged in the workforce or preparing for employment. These outcomes reflect both the opportunities and challenges youth encounter as they work toward economic self-sufficiency and develop job-related skills.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 💼 [**Full-time Employment**](#full-time-employment-variable-description) | **1.1%** | **31.5%** | **31.8%** |
| ⏰ [**Part-time Employment**](#part-time-employment-variable-description) | **10.0%** | **23.6%** | **30.6%** |
| 🛠️ [**Employment Skills Training**](#employment-skills-training-variable-description) | **16.8%** | **37.7%** | **46.5%** |

#### 📈 Analysis:
> **📊 Key Finding:** By age 21, nearly one-third (**31.8%**) of youth have held full-time jobs, and almost half (**46.5%**) have completed employment skills training.
> 
> - ✅ Full-time employment rises by **30.4%** after foster care
> - ✅ Employment skills training participation increases by **20.9%**, indicating many youth seek to build job skills during the transition to adulthood

---
<div style="page-break-after: always;"></div>
---
## 💵 Financial Independence

> **What this domain measures:** This domain evaluates the extent to which youth are able to support themselves financially. These outcomes reflect the financial challenges and reliance on assistance that youth may experience as they move toward independent adulthood. At baseline, youth responses may include financial assistance received from parents or family members.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 💳 [**Receiving Other Financial Assistance**](#receiving-other-financial-assistance-variable-description) | **3.5%** | **7.4%** | **10.6%** |
| 🏛️ [**Receiving Public Financial Assistance**](#receiving-public-financial-assistance-variable-description) | **4.1%** | **5.3%** | **6.0%** |
| 🍽️ [**Receiving Public Food Assistance**](#receiving-public-food-assistance-variable-description) | **5.0%** | **36.6%** | **36.7%** |
| 💰 [**Receiving Social Security Benefits**](#receiving-social-security-benefits-variable-description) | **7.1%** | **9.9%** | **14.9%** |

#### 📈 Analysis:
> **📊 Key Finding:** A combined **68.2%** of youth receive financial assistance before and after transition, showing widespread reliance on multiple support sources.
> 
> - ⚠️ The largest increase in assistance after transition is in **public food assistance**, which rises by **31.6%**
> - ⚠️ Before transition, **7.6%** receive financial assistance (both public and private); after, **12.7%** do

---
<div style="page-break-after: always;"></div>
---
## 🎓 Education & Training

> **What this domain measures:** This domain evaluates the educational progress and engagement of youth by tracking key educational milestones. These indicators reflect both ongoing participation in education and the attainment of credentials that support long-term self-sufficiency and career opportunities.
> 
> **📝 Note:** If a youth reports pursuing a bachelor's degree at baseline and begins pursuing a higher degree or stops pursuing the degree during post-transition, they will answer 'no' to bachelor's degree in the post-transition wave.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 🎓 **Associate Degree** | **0.1%** | **1.9%** | **2.1%** |
| 🎓 **Bachelor Degree** | **0.1%** | **0.0%** | **0.1%** |
| 📚 **Currently Enrolled in School/Training** | **95.4%** | **46.6%** | **96.5%** |
| 💳 **Receiving Educational Aid** | **2.0%** | **17.2%** | **18.5%** |
| 📜 **High School Diploma/GED** | **4.4%** | **59.0%** | **60.7%** |
| 🏆 **Higher Education Certification** | **100.0%** | **69.2%** | **60.9%** |
| 🎓 **Higher Degree** | **0.0%** | **0.3%** | **0.3%** |
| 🔧 **Vocational Certificate** | **0.0%** | **0.0%** | **0.0%** |
| 📋 **Vocational License** | **0.0%** | **0.0%** | **0.0%** |

#### 📈 Analysis:
> **📊 Key Findings:**
> 
> - ✅ High school diploma or GED attainment rises by **54.6%** from baseline to post-transition
> - ✅ Educational aid receipt increases by **15.2%**
> - ⚠️ School or training enrollment drops by **48.8%**
> - ⚠️ Associate and higher degree attainment remains low, with only slight increases post-transition
> - ❌ Vocational certificates and licenses are consistently **0.0%**, showing minimal engagement in these options

---
<div style="page-break-after: always;"></div>
---
## 👨‍👩‍👧‍👦 Family and Children

> **What this domain measures:** This domain assesses the extent to which youth are beginning to form families of their own. These outcomes provide insight into early parenthood and family formation within this population, highlighting important aspects of their transition to adulthood and the support they may need as young parents.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 👶 [**Has Children**](#has-children-variable-description) | **5.9%** | **27.0%** | **28.8%** |
| 💍 [**Married at Child's Birth**](#marriage-variable-description) | **0.0%** | **15.9%** | **14.7%** |

#### 📈 Analysis:
> **📊 Key Finding:** By age 21, **28.8%** of youth in the sample have children, but only **14.7%** were married at the time of their child's birth.
> 
> - 👶 Between ages 18 and 21, more than 1 in 4 youth (**27.0%**) became parents
> - 💍 Only **15.9%** of youth with children were married at the time of their child's birth post-transition, meaning that the vast majority (over **84%**) became parents outside of marriage
> - 📊 Among all youth post-transition, **27.0%** have children, but just **15.9%** were married at the time of their child's birth

---

## 🧑‍🤝‍🧑 Adult Support

> **What this domain measures:** This domain evaluates whether youth have a stable and supportive relationship with at least one adult. This indicator reflects the presence of a caring adult who can offer guidance, emotional support, and practical assistance as youth navigate the challenges of adulthood. Maintaining such connections is considered a key protective factor for positive outcomes during and after the transition from foster care.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 🤝 [**Connection to Supportive Adult**](#connection-to-supportive-adult-variable-description) | **95.3%** | **94.3%** | **99.2%** |

#### 📈 Analysis:
> **📊 Key Finding:** The vast majority of individuals maintain a connection to a supportive adult between ages 17 and 21.

---

## ⚖️ Justice System Involvement

> **What this domain measures:** This domain shows how many youth have been incarcerated.

| Outcome | Baseline (age 17) | Post-Transition (ages 18-21) | Combined |
|---------|:-----------------:|:----------------------------:|:--------:|
| 🔒 [**Experienced Incarceration**](#experienced-incarceration-variable-description) | **44.7%** | **35.7%** | **57.1%** |

#### 📈 Analysis:
> **📊 Key Finding:** Over half of youth in foster care (**57.1%**) have been incarcerated at some point in their lives.
> 
> - ✅ The proportion of youth incarcerated decreases by **9%** after leaving foster care, by age 21

---

*📅 Report generated: July 17, 2025 at 3:00 PM*

---

<div style="page-break-after: always;"></div>

# 📚 Appendix

### 📖 NYTD Outcomes Codebook
See this appendix for Outcome variable names and definitions.

[📄 NYTD Outcomes Codebook (PDF)](https://www.ndacan.acf.hhs.gov/datasets/pdfs_user_guides/nytd-outcomes-codebook.pdf)

---

### 📊 Wave Variable Description
<a name="wave-variable-description"></a>

<a href="#executive-summary" class="back-btn">Back to table</a>

![Wave Variable Description](Wave.png)

---
<div style="page-break-after: always;"></div>

### 🏠 Homeless Variable Description
<a name="homeless-variable-description"></a>

[🔙 Back to table](#🏠-housing-stability)

![Homeless Variable Description](Homeless.png)

---
<div style="page-break-after: always;"></div>

### 🏘️ Public Housing Assistance Variable Description
<a name="public-housing-assistance-variable-description"></a>

[🔙 Back to table](#🏠-housing-stability)

![Public Housing Assistance Variable Description](Housng_assistance_public.png)

---
<div style="page-break-after: always;"></div>

### 💼 Full-time Employment Variable Description
<a name="full-time-employment-variable-description"></a>

[🔙 Back to table](#💼-employment)

![Full-time Employment Variable Description](Full_time_employment.png)

---
<div style="page-break-after: always;"></div>

### ⏰ Part-time Employment Variable Description
<a name="part-time-employment-variable-description"></a>

[🔙 Back to table](#💼-employment)

![Part-time Employment Variable Description](Partime_employment.png)

---
<div style="page-break-after: always;"></div>

### 🛠️ Employment Skills Training Variable Description
<a name="employment-skills-training-variable-description"></a>

[🔙 Back to table](#💼-employment)

![Employment Skills Training Variable Description](Employment_skills_training.png)

---
<div style="page-break-after: always;"></div>

### 🤝 Connection to Supportive Adult Variable Description
<a name="connection-to-supportive-adult-variable-description"></a>

[🔙 Back to table](#🧑‍🤝‍🧑-adult-support)

![Connection to Supportive Adult Variable Description](Connection%20to%20Supportive%20Adult.png)

---
<div style="page-break-after: always;"></div>

### 🔒 Experienced Incarceration Variable Description
<a name="experienced-incarceration-variable-description"></a>

[🔙 Back to table](#⚖️-justice-system-involvement)

![Experienced Incarceration Variable Description](Experienced%20Incarceration.png)

---
<div style="page-break-after: always;"></div>

### 👶 Has Children Variable Description
<a name="has-children-variable-description"></a>

[🔙 Back to table](#👨‍👩‍👧‍👦-family-and-children)

![Has Children Variable Description](Has%20Children.png)

---
<div style="page-break-after: always;"></div>

### 💍 Marriage Variable Description
<a name="marriage-variable-description"></a>

[🔙 Back to table](#👨‍👩‍👧‍👦-family-and-children)

![Marriage Variable Description](Marriage.png)

---
<div style="page-break-after: always;"></div>

### 💳 Receiving Other Financial Assistance Variable Description
<a name="receiving-other-financial-assistance-variable-description"></a>

[🔙 Back to table](#💵-financial-independence)

![Receiving Other Financial Assistance Variable Description](Receiving%20Other%20Financial%20Assistance.png)

---
<div style="page-break-after: always;"></div>

### 🏛️ Receiving Public Financial Assistance Variable Description
<a name="receiving-public-financial-assistance-variable-description"></a>

[🔙 Back to table](#💵-financial-independence)

![Receiving Public Financial Assistance Variable Description](Receiving%20Public%20Financial%20Assistance.png)

---
<div style="page-break-after: always;"></div>

### 🍽️ Receiving Public Food Assistance Variable Description
<a name="receiving-public-food-assistance-variable-description"></a>

[🔙 Back to table](#💵-financial-independence)

![Receiving Public Food Assistance Variable Description](Receiving%20Public%20Food%20Assistance.png)

---
<div style="page-break-after: always;"></div>

### 💰 Receiving Social Security Benefits Variable Description
<a name="receiving-social-security-benefits-variable-description"></a>

[🔙 Back to table](#💵-financial-independence)

![Receiving Social Security Benefits Variable Description](Receiving%20Social%20Security%20Benefits.png)

---
<div style="page-break-after: always;"></div>

### 🏥 Substance Abuse Referral Variable Description
<a name="substance-abuse-referral-variable-description"></a>

[🔙 Back to table](#🏥-health--wellness)

![Substance Abuse Referral Variable Description](Substance%20Abuse%20Referral.png)

---
<div style="page-break-after: always;"></div>

### 🎓 Education Variable Description
<a name="education-variable-description"></a>

[🔙 Back to table](#🎓-education--training)

![Higher Education Certification Variable Description](Higher%20education.png)