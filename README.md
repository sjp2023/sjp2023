### Welcome 👋
## Health Data Analysis Portfolio

🌱 Hi — I'm [Sky Suh], a health data informatics professional with a background in [Bachelor of Information, previously Population Health and Mental Health]. This repository collects my independent data analysis work using publicly available datasets from the WHO, UNICEF, WFP, and other global health organizations.

# Why I build up this health informatics portfolio with Non-Profit Organization
⚡ Most of what ends up here started as a question I couldn't find a clean answer to with precise data analysis that can support the understand and well present of the health crisis. The projects range from descriptive epidemiology to correlation analysis to SQL-based health burden work. Tools vary by project including R, Python, Pandas, SQL, Matplotlib, Seaborn, SciPy for covering the health burden and its data.

---

## Projects

| # | Project | Data Source | Tools | Key Question |
|---|---|---|---|---|
| 1 | [Under-5 Child Mortality Trends (2000–2022)](./project1_child_mortality/) | UNICEF / WHO GHO | Python, Pandas, Matplotlib | Which regions are on track for SDG 3.2, and which are falling behind? |
| 2 | [The Mental Health Treatment Gap](./project2_mental_health/) | WHO Mental Health Atlas 2020 | Python, SciPy, Seaborn | What resource inputs predict a smaller treatment gap? |
| 3 | [Vaccine Coverage & COVID-19 Disruption](./project3_vaccine_coverage/) | WHO-UNICEF WUENIC 2022 | Python, Matplotlib | How badly did the pandemic set back routine immunization? |
| 4 | [Food Insecurity & Child Stunting](./project4_nutrition_wfp/) | WFP HungerMap · UNICEF JME | Python, Seaborn, SciPy | Where does food insecurity translate into stunting — and where doesn't it? |
| 5 | [NCD Double Burden: SQL Analysis](./project5_disease_burden/) | WHO GHE 2020 · GBD Study | Python, SQLite, Seaborn | Which countries face simultaneous high burdens of NCDs and infectious disease? |

---

## Skills Demonstrated

**Analysis:** Descriptive statistics · Correlation analysis (Pearson, Spearman) · Trend analysis · Time series · Stratified comparison · Counterfactual modeling

**SQL:** Window functions · CTEs · Conditional aggregation · Multi-table JOINs · In-memory SQLite databases

**Visualization:** Multi-panel figures · Scatter plots with regression · Heatmaps · Stacked bar charts · Trend lines with uncertainty shading

**Domain:** Global health epidemiology · SDG tracking · Immunization systems · Nutritional anthropometrics · Disease burden (DALY framework) · Health system financing

---

## Data Transparency

All projects use publicly available data from recognized international organizations. Where I've simulated or modelled data to match published aggregate estimates (due to file size or format constraints), I've documented this clearly in each project's README, including the original source URL.

No proprietary or patient-level data is used anywhere in this repository.

---

## Running the Code

Each project is self-contained. Install dependencies once:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

Then run any project:

```bash
cd project1_child_mortality
python analysis.py
```

---

## Contact
📫 Feel free to contact me through this!:
[http://linkedin.com/in/sky-suh-656644237] · [suhjeongpin@gmail.com] 

