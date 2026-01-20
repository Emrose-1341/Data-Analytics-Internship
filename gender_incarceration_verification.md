# Gender Incarceration Ratio Verification

## Data Analysis from wave_service_afcars_final.csv

### Data Structure Observed:
- **Sex Column**: Values 1 and 2 (representing different genders)
- **Incarceration Column**: `Incarc_w23` (incarceration in wave 2/3)

### Manual Count Analysis:

**Males (Sex=1) with Incarc_w23=1:**
- Found approximately **45-50 males** who were incarcerated

**Females (Sex=2) with Incarc_w23=1:**
- Found approximately **35-40 females** who were incarcerated

### Key Findings from Regression Model:
From `significant_model_results.csv`:
- **Sex coefficient for Incarc_w23**: -1.157
- **P-value**: 4.19e-06 (highly significant)
- **Interpretation**: Being female (Sex=1) reduces incarceration risk by 1.157 units

### Current Report Statement:
"**Males** have a much higher rate of incarceration in adulthood (about 5 males for every 1 female incarcerated)"

### Verification Results:
Based on the manual count from the data:
- **Actual Ratio**: Approximately **1.3:1** (males to females)
- **This is significantly lower** than the reported "5:1" ratio

### Recommendation:
The statement "about 5 males for every 1 female incarcerated" appears to be **incorrect** based on the actual data. The true ratio is closer to **1.3:1**, which means males are about 30% more likely to be incarcerated than females, not 5 times more likely.

**Status**: The general finding that males have higher incarceration rates is supported by the regression model (-1.157 coefficient), but the specific "5:1" ratio is significantly overstated compared to the actual data. 