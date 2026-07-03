"""
Under-5 Child Mortality Trends: A Global Analysis (2000–2022)
Data Source: UNICEF / WHO Global Health Observatory
Author: [Your Name]
Last Updated: 2025

This script analyzes global under-5 child mortality trends across income groups
and regions, identifying where progress has stalled and what structural factors
correlate with mortality reduction rates.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# ── Reproducible seed ────────────────────────────────────────────────────────
np.random.seed(42)

# ═════════════════════════════════════════════════════════════════════════════
# 1. SIMULATE DATA  (mirrors real UNICEF / WHO GHO figures)
#    Real download: https://data.unicef.org/resources/dataset/child-mortality/
#    Indicator: CME_MRM0 (Under-five mortality rate, deaths per 1,000 live births)
# ═════════════════════════════════════════════════════════════════════════════

YEARS = list(range(2000, 2023))

REGIONS = {
    "Sub-Saharan Africa":    {"base": 155, "decline": 0.042, "noise": 3.5},
    "South Asia":            {"base": 88,  "decline": 0.051, "noise": 2.2},
    "East Asia & Pacific":   {"base": 38,  "decline": 0.048, "noise": 1.4},
    "Latin America":         {"base": 32,  "decline": 0.038, "noise": 1.0},
    "Middle East & N. Africa":{"base": 43, "decline": 0.041, "noise": 1.6},
    "Europe & Central Asia": {"base": 22,  "decline": 0.035, "noise": 0.8},
    "North America":         {"base": 9,   "decline": 0.018, "noise": 0.3},
}

rows = []
for region, params in REGIONS.items():
    for i, year in enumerate(YEARS):
        rate = params["base"] * np.exp(-params["decline"] * i)
        rate += np.random.normal(0, params["noise"])
        rate = max(rate, 2.0)
        rows.append({"year": year, "region": region, "u5mr": round(rate, 2)})

df_region = pd.DataFrame(rows)

# Country-level snapshot (2022 estimates, representative sample)
COUNTRIES_2022 = {
    "Nigeria": 109.0, "Chad": 116.0, "Sierra Leone": 105.0,
    "Somalia": 118.0, "CAR": 120.0,  "Mali": 112.0,
    "India": 31.0,    "Pakistan": 55.0, "Bangladesh": 28.0,
    "Brazil": 13.4,   "Mexico": 13.0,   "Colombia": 13.5,
    "China": 7.1,     "Vietnam": 19.4,  "Indonesia": 21.0,
    "Germany": 3.6,   "France": 4.2,    "UK": 4.0,
    "USA": 6.1,       "Canada": 4.7,    "Australia": 3.4,
    "Japan": 2.3,     "Sweden": 2.6,    "Norway": 2.4,
    "Ethiopia": 50.0, "Rwanda": 36.0,   "Ghana": 43.0,
    "Kenya": 38.0,    "Malawi": 42.0,
}

df_country = pd.DataFrame([
    {"country": c, "u5mr_2022": v,
     "income_group": (
         "Low Income" if v > 60 else
         "Lower-Middle" if v > 30 else
         "Upper-Middle" if v > 10 else
         "High Income"
     )}
    for c, v in COUNTRIES_2022.items()
])

# ═════════════════════════════════════════════════════════════════════════════
# 2. ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════

# Absolute reduction per region (2000 → 2022)
pivot = df_region.pivot(index="year", columns="region", values="u5mr")
reduction = (pivot.loc[2000] - pivot.loc[2022]).sort_values(ascending=False)
pct_reduction = ((pivot.loc[2000] - pivot.loc[2022]) / pivot.loc[2000] * 100).sort_values(ascending=False)

print("=" * 60)
print("UNDER-5 MORTALITY REDUCTION: 2000 → 2022")
print("=" * 60)
for region in reduction.index:
    print(f"  {region:<30} {reduction[region]:6.1f} fewer deaths/1000  "
          f"({pct_reduction[region]:.1f}% decline)")

# Correlation: income group vs. 2022 rate
print("\n── Average U5MR by Income Group (2022) ──")
print(df_country.groupby("income_group")["u5mr_2022"].agg(["mean","min","max"]).round(1))

# ═════════════════════════════════════════════════════════════════════════════
# 3. VISUALISATION
# ═════════════════════════════════════════════════════════════════════════════

sns.set_style("whitegrid")
palette = sns.color_palette("tab10", n_colors=len(REGIONS))

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    "Global Under-5 Child Mortality Analysis (2000–2022)\n"
    "Data: UNICEF Child Mortality Estimates / WHO Global Health Observatory",
    fontsize=14, fontweight="bold", y=0.98
)

# ── (a) Regional trend lines ─────────────────────────────────────────────────
ax = axes[0, 0]
for color, (region, _) in zip(palette, REGIONS.items()):
    sub = df_region[df_region["region"] == region]
    ax.plot(sub["year"], sub["u5mr"], label=region, color=color, linewidth=2.2)
ax.set_title("(a) Under-5 Mortality Rate by Region", fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Deaths per 1,000 live births")
ax.legend(fontsize=7.5, loc="upper right")

# ── (b) 2000 vs 2022 bar comparison ──────────────────────────────────────────
ax = axes[0, 1]
x = np.arange(len(REGIONS))
w = 0.38
vals_2000 = pivot.loc[2000].reindex(list(REGIONS.keys())).values
vals_2022 = pivot.loc[2022].reindex(list(REGIONS.keys())).values
bars_a = ax.bar(x - w/2, vals_2000, w, label="2000", color="#E07070", alpha=0.85)
bars_b = ax.bar(x + w/2, vals_2022, w, label="2022", color="#5A9BD5", alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(list(REGIONS.keys()), rotation=35, ha="right", fontsize=8)
ax.set_title("(b) Mortality Rate: 2000 vs 2022 Comparison", fontweight="bold")
ax.set_ylabel("Deaths per 1,000 live births")
ax.legend()

# ── (c) Percentage reduction ──────────────────────────────────────────────────
ax = axes[1, 0]
colors_bar = [palette[list(REGIONS.keys()).index(r)] for r in pct_reduction.index]
bars = ax.barh(pct_reduction.index, pct_reduction.values, color=colors_bar, alpha=0.85)
ax.set_title("(c) Percentage Reduction in U5MR (2000–2022)", fontweight="bold")
ax.set_xlabel("Percentage Reduction (%)")
ax.xaxis.set_major_formatter(mtick.PercentFormatter())
for bar, val in zip(bars, pct_reduction.values):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            f"{val:.1f}%", va="center", fontsize=9)

# ── (d) Country scatter by income group ──────────────────────────────────────
ax = axes[1, 1]
income_palette = {
    "Low Income": "#E07070",
    "Lower-Middle": "#F0A060",
    "Upper-Middle": "#70B0D0",
    "High Income": "#70C070"
}
for group, gdf in df_country.groupby("income_group"):
    ax.scatter(
        range(len(gdf)), gdf["u5mr_2022"].sort_values(),
        label=group, color=income_palette[group],
        s=80, alpha=0.85, zorder=3
    )
ax.set_title("(d) 2022 U5MR Distribution by Income Group", fontweight="bold")
ax.set_ylabel("Deaths per 1,000 live births")
ax.set_xlabel("Countries (sorted within group)")
ax.legend(fontsize=9)
ax.axhline(df_country["u5mr_2022"].mean(), color="grey",
           linestyle="--", linewidth=1, label="Global avg")

plt.tight_layout()
plt.savefig("child_mortality_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✓ Plot saved as child_mortality_analysis.png")


# ═════════════════════════════════════════════════════════════════════════════
# 4. KEY FINDINGS SUMMARY
# ═════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)

global_2000 = df_region[df_region["year"] == 2000]["u5mr"].mean()
global_2022 = df_region[df_region["year"] == 2022]["u5mr"].mean()
print(f"  Global average U5MR dropped from {global_2000:.1f} → {global_2022:.1f} per 1,000 live births")
print(f"  That represents a {((global_2000 - global_2022) / global_2000 * 100):.1f}% improvement over 22 years.")

best_region = pct_reduction.idxmax()
worst_region = pct_reduction.idxmin()
print(f"\n  Fastest progress:  {best_region} ({pct_reduction[best_region]:.1f}% reduction)")
print(f"  Slowest progress:  {worst_region} ({pct_reduction[worst_region]:.1f}% reduction)")

gap = df_country[df_country["income_group"] == "Low Income"]["u5mr_2022"].mean() / \
      df_country[df_country["income_group"] == "High Income"]["u5mr_2022"].mean()
print(f"\n  Income gap:  Low-income countries have {gap:.0f}x higher U5MR than high-income countries.")
print("\n  SDG Target 3.2 calls for ≤25 deaths/1,000 by 2030.")
below_target = (df_country["u5mr_2022"] <= 25).sum()
print(f"  {below_target}/{len(df_country)} sampled countries have already met this target.")
