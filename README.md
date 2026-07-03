# Under-5 Child Mortality Trends: A Global Analysis (2000–2022)

**Data Source:** UNICEF Child Mortality Estimates · WHO Global Health Observatory  
**Tools:** Python · Pandas · Matplotlib · Seaborn · SciPy  
**Status:** Complete

---

## Why This Project

Every year, millions of children under five die from causes that are largely preventable — pneumonia, diarrhea, malaria, complications at birth. The gap between what's happening and what's *possible* is one of the clearest indicators of health system inequality worldwide.

I built this analysis because the raw numbers tell only part of the story. The more interesting question is: **which regions have closed the gap fastest, and what does that trajectory mean for SDG 3.2 targets by 2030?**

---

## Dataset

| Field | Details |
|---|---|
| Indicator | Under-5 Mortality Rate (U5MR) — deaths per 1,000 live births |
| Time span | 2000–2022 |
| Granularity | Regional aggregates + country-level 2022 snapshot |
| Source | UNICEF CME database · WHO GHO Indicator `CME_MRM0` |
| Access | https://data.unicef.org/resources/dataset/child-mortality/ |

---

## What I Did

1. **Data loading & cleaning** — handled missing values and inconsistent region classifications across source files
2. **Trend analysis** — fitted exponential decay curves to quantify annual decline rates per region
3. **Comparative analysis** — 2000 vs. 2022 absolute and percentage reduction by region
4. **Income-group stratification** — classified countries by World Bank income tier; tested distribution differences
5. **SDG progress check** — identified how many countries are on track for the 2030 target of ≤25/1,000

---

## Key Findings

- **Global U5MR fell ~55% between 2000 and 2022**, from roughly 76 to 34 deaths per 1,000 live births
- **South Asia showed the fastest proportional decline** (~68%), largely driven by improvements in India and Bangladesh
- **Sub-Saharan Africa** still carries the highest burden (~80 deaths/1,000) despite meaningful absolute reductions
- **Income gap persists**: low-income countries have approximately **20× higher U5MR** than high-income countries as of 2022
- At current trajectories, **Sub-Saharan Africa is unlikely to meet SDG 3.2 by 2030** without accelerated investment in community health workers and nutrition programs

---

## Files

```
project1_child_mortality/
├── analysis.py              # Main analysis script
├── child_mortality_analysis.png  # Output visualization
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scipy
python analysis.py
```

---

## Further Reading

- UNICEF (2023). *Levels and Trends in Child Mortality Report 2023.*
- WHO Global Health Observatory: https://www.who.int/data/gho
- SDG Target 3.2: https://sdgs.un.org/goals/goal3
