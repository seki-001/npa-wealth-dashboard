"""
NPA Presentation — NRM MPs Retreat Kyankwanzi, April 2026
"Achieving Higher Middle-Income Status for Uganda: The NRM Government's Strategy for 10-Fold Growth"
Prof. Pamela K. Mbabazi | National Planning Authority

Visualizations covering:
  1.  Vision 2040 vs 10-Fold GDP Trajectory
  2.  Vision 2040 Targets — Before vs After
  3.  NDP Timeline (2010–2040)
  4.  NDPIV High-Impact Projects by Priority Area
  5.  NDPIV Macro Outlook Targets
  6.  Agro-Industrialisation Programme Results
  7.  Tourism Development Programme Results
  8.  Extractives Industry Programme Results
  9.  Private Sector Development Results
 10.  Lending Rate Reduction Targets
 11.  Innovation / STI Programme Results
 12.  ATMS Strategic Priority Areas — Target Revenue
 13.  Economic Structure Shift (Agriculture vs Industry)
 14.  Labour Force Shift (Agriculture vs Industry)
 15.  Summary Dashboard — All Key Metrics

Requirements: pip install matplotlib numpy pandas
"""

import matplotlib
matplotlib.use("Agg")          # remove if running interactively
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import os

# ── Output folder ───────────────────────────────────────────────────────────
OUT = "npa_charts"
os.makedirs(OUT, exist_ok=True)

# ── Palette ─────────────────────────────────────────────────────────────────
NAVY   = "#0F3460"
DARK   = "#16213E"
GREEN  = "#1B6B3A"
AMBER  = "#B45309"
RED    = "#B91C1C"
TEAL   = "#0E7490"
PURPLE = "#6D28D9"
OLIVE  = "#4D7C0F"
GRAY   = "#6B7280"
LGRAY  = "#F1F5F9"
WHITE  = "#FFFFFF"
GOLD   = "#CA8A04"

PALETTE = [NAVY, GREEN, AMBER, TEAL, PURPLE, RED, OLIVE, GOLD]

plt.rcParams.update({
    "font.family":       "DejaVu Sans",
    "font.size":         9.5,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "grid.color":        "#E5E7EB",
    "grid.linewidth":    0.6,
    "axes.axisbelow":    True,
    "figure.facecolor":  WHITE,
    "axes.facecolor":    WHITE,
    "axes.edgecolor":    "#CBD5E1",
    "xtick.color":       "#374151",
    "ytick.color":       "#374151",
    "text.color":        "#111827",
})

def save(fig, name):
    path = f"{OUT}/{name}.png"
    fig.savefig(path, dpi=160, bbox_inches="tight",
                facecolor=WHITE, edgecolor="none")
    plt.close(fig)
    print(f"  ✓  {name}.png")

def bar_labels(ax, bars, fmt="{:.0f}", offset_frac=0.01, fontsize=8.5, color=None):
    """Add value labels on top of bars."""
    ymax = ax.get_ylim()[1]
    offset = ymax * offset_frac
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                h + offset,
                fmt.format(h),
                ha="center", va="bottom",
                fontsize=fontsize, fontweight="bold",
                color=color or bar.get_facecolor(),
            )

def hbar_labels(ax, bars, fmt="{:.1f}", offset=0.3, fontsize=8.5):
    for bar in bars:
        w = bar.get_width()
        if w > 0:
            ax.text(
                w + offset,
                bar.get_y() + bar.get_height() / 2,
                fmt.format(w),
                va="center", fontsize=fontsize, fontweight="bold",
            )

# ════════════════════════════════════════════════════════════════════════════
# 1. GDP TRAJECTORY — Vision 2040 vs 10-Fold Growth Strategy
# ════════════════════════════════════════════════════════════════════════════
print("Chart 1: GDP Trajectory")

years        = [2010, 2015, 2020, 2022, 2025, 2030, 2035, 2040]
gdp_actual   = [17,   26,   38,   47,   60,   None, None, None]   # USD bn
gdp_vision   = [17,   None, None, None, None, None, None, 580.5]  # end target
# 10-fold: 60→600 in 15 years (2025→2040), NDPIV doubles by 2030 (60→158)
gdp_10fold   = [None, None, None, None, 60,   158,  350,  600]
# Baseline (7% avg growth from 60 → ~84→118→165)
gdp_baseline = [None, None, None, None, 60,   84,   118,  166]

fig, ax = plt.subplots(figsize=(12, 6))

# Plot series
ax.plot([y for y, v in zip(years, gdp_actual)   if v],
        [v for v in gdp_actual   if v], color=NAVY,  lw=2.5, marker="o", ms=6, label="Historical GDP (USD bn)")
ax.plot([y for y, v in zip(years, gdp_baseline) if v],
        [v for v in gdp_baseline if v], color=GRAY,  lw=2,   ls="--", marker="s", ms=5, label="Baseline 7% growth path")
ax.plot([y for y, v in zip(years, gdp_10fold)   if v],
        [v for v in gdp_10fold   if v], color=GREEN, lw=3,   marker="^", ms=7, label="10-Fold Growth Strategy (target)")

# Milestones
ax.annotate("Vision 2040\nTarget: USD 580.5bn", xy=(2040, 580.5),
            xytext=(2033, 500), fontsize=8.5, color=DARK,
            arrowprops=dict(arrowstyle="->", color=DARK, lw=1.2))
ax.annotate("10-Fold Target\nUSD 600bn", xy=(2040, 600),
            xytext=(2033, 430), fontsize=8.5, color=GREEN,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
ax.annotate("NDPIV doubles GDP\nto USD 158bn by 2030", xy=(2030, 158),
            xytext=(2024, 200), fontsize=8.5, color=GREEN,
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
ax.annotate("Current GDP\nUSD 60bn (2025)", xy=(2025, 60),
            xytext=(2018, 90), fontsize=8.5, color=NAVY,
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))

ax.set_xlabel("Year", fontsize=10)
ax.set_ylabel("GDP (USD Billions)", fontsize=10)
ax.set_title("Uganda GDP Trajectory: Historical, Baseline & 10-Fold Growth Strategy",
             fontsize=13, fontweight="bold", pad=12, loc="left", color=DARK)
ax.legend(fontsize=9, loc="upper left")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}bn"))
ax.set_xlim(2008, 2043)
ax.set_ylim(0, 680)

fig.text(0.5, -0.02,
         "Source: NPA Presentation, Kyankwanzi April 2026 | Vision 2040 | NDPIV",
         ha="center", fontsize=8, color=GRAY, style="italic")
save(fig, "01_gdp_trajectory")

# ════════════════════════════════════════════════════════════════════════════
# 2. VISION 2040 TARGETS — Before vs After (grouped bars)
# ════════════════════════════════════════════════════════════════════════════
print("Chart 2: Vision 2040 Targets")

metrics  = ["GDP\n(USD bn)", "Per Capita\nIncome (USD)",
            "Population\nBelow Poverty (%)", "Agriculture\n% of GDP",
            "Industry\n% of GDP", "Manufactured\nGoods in Exports (%)",
            "Agri Labour\nForce (%)", "Industry\nLabour Force (%)",
            "Patents\nRegistered/yr"]
baseline = [17,    506,   24.5, 53.1,  9.5,  4.2,  65.6,  7.6,   3]
target   = [580.5, 9500,  5,    10.4,  31.4, 50,   31,    26,    6000]

# Normalise for display (some metrics are 'lower is better')
lower_better = {2, 3, 6}   # indices where lower = better

fig, axes = plt.subplots(3, 3, figsize=(16, 13))
axes = axes.flatten()

for i, (m, b, t) in enumerate(zip(metrics, baseline, target)):
    ax = axes[i]
    lb = i in lower_better
    cols = [AMBER, GREEN] if not lb else [GREEN, RED]
    bars = ax.bar(["Baseline\n(2010)", "Target\n(2040)"], [b, t],
                  color=cols, width=0.45, zorder=3)
    # annotate bars
    for bar, val in zip(bars, [b, t]):
        lbl = f"{val:,.0f}" if val >= 100 else f"{val:.1f}"
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.03,
                lbl, ha="center", fontsize=9, fontweight="bold",
                color=bar.get_facecolor())
    change = ((t - b) / b * 100) if b > 0 else 0
    direction = "▼" if lb else "▲"
    ax.set_title(m, fontsize=9.5, fontweight="bold", color=DARK)
    ax.text(0.98, 0.92,
            f"{direction} {abs(change):.0f}%",
            transform=ax.transAxes, ha="right", fontsize=9,
            color=GREEN if not lb else RED, fontweight="bold")
    ax.set_ylim(0, max(b, t) * 1.25)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(
        lambda v, _: f"{v:,.0f}" if v >= 1000 else f"{v:.0f}"))

fig.suptitle("Vision 2040 Targets: Baseline (2010) vs. 2040 Goals",
             fontsize=14, fontweight="bold", y=1.01, color=DARK)
fig.tight_layout(rect=[0, 0.02, 1, 1])
fig.text(0.5, -0.01,
         "Source: NPA / Vision 2040 | Lower-is-better metrics shown in green→red",
         ha="center", fontsize=8, color=GRAY, style="italic")
save(fig, "02_vision2040_targets")

# ════════════════════════════════════════════════════════════════════════════
# 3. NDP TIMELINE (Gantt-style)
# ════════════════════════════════════════════════════════════════════════════
print("Chart 3: NDP Timeline")

ndps = [
    ("NDP I",   2010.5, 2014.5, "Completed", GREEN),
    ("NDP II",  2015.5, 2019.5, "Completed", GREEN),
    ("NDP III", 2020.5, 2024.5, "Running",   AMBER),
    ("NDP IV",  2025.5, 2029.5, "Running",   TEAL),
    ("NDP V",   2030.5, 2034.5, "Not Yet",   GRAY),
    ("NDP VI",  2035.5, 2039.5, "Not Yet",   GRAY),
]
phases = [
    ("Phase 1: Fundamental\nEconomic Reforms", 1986, 1996, "#CBD5E1"),
    ("Phase 2: PEAP\n(Poverty Eradication)", 1997, 2009, "#BAE6FD"),
    ("Phase 3: Growth &\nSocio-Economic\nTransformation", 2010, 2040, "#BBF7D0"),
]

fig, ax = plt.subplots(figsize=(14, 6))

# Phase bands
for label, start, end, col in phases:
    ax.axvspan(start, end, alpha=0.15, color=col, lw=0)
    ax.text((start + end) / 2, 7.6, label, ha="center", fontsize=8,
            color=GRAY, style="italic")

# NDP bars
for i, (name, start, end, status, col) in enumerate(ndps):
    ax.barh(i, end - start, left=start, height=0.55,
            color=col, alpha=0.85, zorder=3)
    ax.text((start + end) / 2, i, f"{name}\n({status})",
            ha="center", va="center", fontsize=8.5, color=WHITE,
            fontweight="bold")

# 10-fold bracket
ax.annotate("", xy=(2040, -0.9), xytext=(2025, -0.9),
            arrowprops=dict(arrowstyle="<->", color=RED, lw=2))
ax.text(2032.5, -1.25, "10-Fold Growth Strategy Period (15 yrs)",
        ha="center", fontsize=9, color=RED, fontweight="bold")

ax.set_yticks(range(len(ndps)))
ax.set_yticklabels([n[0] for n in ndps], fontsize=10)
ax.set_xlim(1984, 2042)
ax.set_ylim(-1.6, 8.2)
ax.set_xlabel("Year", fontsize=10)
ax.set_title("Uganda Comprehensive Integrated National Development Planning Framework\n"
             "Six 5-Year NDPs under Vision 2040 (2010–2040)",
             fontsize=12, fontweight="bold", pad=10, loc="left", color=DARK)
ax.grid(axis="y", alpha=0)
ax.grid(axis="x")

patches = [mpatches.Patch(color=GREEN, label="Completed"),
           mpatches.Patch(color=AMBER, label="Currently Running"),
           mpatches.Patch(color=TEAL,  label="Running (NDPIV)"),
           mpatches.Patch(color=GRAY,  label="Not Yet Started")]
ax.legend(handles=patches, fontsize=8.5, loc="lower right")
save(fig, "03_ndp_timeline")

# ════════════════════════════════════════════════════════════════════════════
# 4. NDPIV HIGH-IMPACT PROJECTS by Priority Area
# ════════════════════════════════════════════════════════════════════════════
print("Chart 4: NDPIV High-Impact Projects")

priority_areas = [
    "Integrated Transport\nInfrastructure & Services",
    "Sustainable Energy\nDevelopment",
    "Human Capital\nDevelopment",
    "Knowledge Economy\n(STI) incl. ICT",
    "Sustainable\nExtractivies",
    "Agro-\nIndustrialisation",
    "Cultural, Creative\n& Sports",
    "Human Capital\nUrban & Housing",
    "Tourism\nDevelopment",
    "Private Sector\nDevelopment",
    "Full Monetization\nof Economy",
    "Manufacturing",
]
n_projects = [15, 13, 9, 6, 5, 4, 3, 2, 3, 1, 1, 1]
cols_proj = [PALETTE[i % len(PALETTE)] for i in range(len(priority_areas))]

sorted_pairs = sorted(zip(n_projects, priority_areas, cols_proj), reverse=True)
n_s, a_s, c_s = zip(*sorted_pairs)

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(a_s, n_s, color=c_s, zorder=3, height=0.6)
for bar, val in zip(bars, n_s):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            str(val), va="center", fontsize=9.5, fontweight="bold")
ax.set_xlabel("Number of High-Impact Projects", fontsize=10)
ax.set_title("NDPIV High-Impact Projects by Priority Area\n"
             "Total: 63 Projects across 12 Priority Areas",
             fontsize=12, fontweight="bold", pad=10, loc="left", color=DARK)
ax.set_xlim(0, 19)
ax.text(0.98, 0.02, "Total: 63 projects",
        transform=ax.transAxes, ha="right", fontsize=10,
        fontweight="bold", color=DARK)
save(fig, "04_ndpiv_projects")

# ════════════════════════════════════════════════════════════════════════════
# 5. NDPIV MACRO OUTLOOK TARGETS (by 2029/30)
# ════════════════════════════════════════════════════════════════════════════
print("Chart 5: NDPIV Macro Targets")

macro_labels   = ["Poverty Rate (%)", "GDP Growth (%)", "Per Capita Income\n(USD)",
                  "Annual Jobs\nCreated (000s)", "Inflation\nTarget (%)",
                  "Revenue-to-GDP\nRatio (%)"]
macro_baseline = [16.9, 5.5, 1154, 500, 5.0, 14.0]   # approx current
macro_target   = [12.9, 10.1, 2942, 885, 5.0, 18.3]
lower_b2       = {0, 4}   # poverty and inflation — lower is better

fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()

for i, (lbl, b, t) in enumerate(zip(macro_labels, macro_baseline, macro_target)):
    ax = axes[i]
    lb = i in lower_b2
    c_base = AMBER if not lb else GREEN
    c_tgt  = GREEN if not lb else RED
    bars = ax.bar(["Current\n(~FY2024/25)", "Target\n(FY2029/30)"],
                  [b, t], color=[c_base, c_tgt], width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        fmt = f"{val:,.0f}" if val > 100 else f"{val:.1f}"
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04, fmt,
                ha="center", fontsize=9.5, fontweight="bold",
                color=bar.get_facecolor())
    chg = ((t - b) / b * 100)
    sym = "▼" if (lb and t < b) or (not lb and t < b) else "▲"
    ax.text(0.97, 0.93, f"{sym} {abs(chg):.0f}%",
            transform=ax.transAxes, ha="right", fontsize=9.5,
            color=c_tgt, fontweight="bold")
    ax.set_title(lbl, fontsize=10, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.3)

fig.suptitle("NDPIV National Development Outlook Targets (FY2029/30)",
             fontsize=13, fontweight="bold", y=1.01, color=DARK)
fig.tight_layout()
fig.text(0.5, -0.01,
         "Source: NPA / NDPIV Outlook | Jobs target: ~885,000 per year",
         ha="center", fontsize=8, color=GRAY, style="italic")
save(fig, "05_ndpiv_macro_targets")

# ════════════════════════════════════════════════════════════════════════════
# 6. AGRO-INDUSTRIALISATION Programme Results
# ════════════════════════════════════════════════════════════════════════════
print("Chart 6: Agro-Industrialisation Results")

agro_metrics = [
    "Agriculture Sector\nGrowth Rate (%)",
    "Export Value of Priority\nCommodities (USD mn)",
    "Import Value of\nAgro-products (USD mn)",
    "Food & Nutrition\nSecurity (%)",
    "Agri Financing\nShare of Total (%)",
    "Annual Jobs from\nAgro-processing (000s)",
]
agro_base = [5.1,  2500, 1096, 71,  11.3, 0]
agro_tgt  = [8.0,  4800, 600,  85,  15.0, 60]
agro_lb   = {2}   # import value — lower is better

fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()
for i, (lbl, b, t) in enumerate(zip(agro_metrics, agro_base, agro_tgt)):
    ax = axes[i]
    lb = i in agro_lb
    cols = ([AMBER, GREEN] if not lb else [GREEN, RED])
    bars = ax.bar(["Baseline\n(FY2023/24)", "Target\n(NDPIV)"],
                  [b, t], color=cols, width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        fmt = f"{val:,.0f}" if val >= 100 else f"{val:.1f}"
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04, fmt,
                ha="center", fontsize=9.5, fontweight="bold",
                color=bar.get_facecolor())
    if b > 0:
        chg = ((t - b) / b * 100)
        sym = "▼" if lb else "▲"
        ax.text(0.97, 0.93, f"{sym} {abs(chg):.0f}%",
                transform=ax.transAxes, ha="right", fontsize=9.5,
                color=GREEN if not lb else RED, fontweight="bold")
    ax.set_title(lbl, fontsize=10, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.3)

fig.suptitle("Agro-Industrialisation Programme: Baseline vs. NDPIV Targets",
             fontsize=13, fontweight="bold", y=1.01, color=DARK)
fig.tight_layout()
fig.text(0.5, -0.01,
         "Focus on 6 value chains: Dairy, Sugar, Coffee, Vegetable Oils, Cassava & Fish",
         ha="center", fontsize=8.5, color=GRAY, style="italic")
save(fig, "06_agro_results")

# ════════════════════════════════════════════════════════════════════════════
# 7. TOURISM DEVELOPMENT Programme Results
# ════════════════════════════════════════════════════════════════════════════
print("Chart 7: Tourism Results")

tour_metrics = [
    "Foreign Exchange\nEarnings (USD bn)",
    "Tourist Length\nof Stay (nights)",
    "Average Spend per\nLeisure Tourist (USD)",
    "Tourist Satisfaction\nScore (%)",
    "Domestic Tourism\nExpenditure (UGX bn)",
    "Programme\nPerformance (%)",
]
tour_base = [1.0,   7.6,  1550, 79,   3675, 57.7]
tour_tgt  = [10.0,  14.0, 3100, 85,   7350, 70.0]

fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()
for i, (lbl, b, t) in enumerate(zip(tour_metrics, tour_base, tour_tgt)):
    ax = axes[i]
    bars = ax.bar(["Baseline\n(FY2023/24)", "Target\n(NDPIV)"],
                  [b, t], color=[AMBER, GREEN], width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        fmt = f"{val:,.0f}" if val >= 100 else f"{val:.1f}"
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04, fmt,
                ha="center", fontsize=9.5, fontweight="bold",
                color=bar.get_facecolor())
    chg = ((t - b) / b * 100)
    ax.text(0.97, 0.93, f"▲ {chg:.0f}%",
            transform=ax.transAxes, ha="right", fontsize=9.5,
            color=GREEN, fontweight="bold")
    ax.set_title(lbl, fontsize=10, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.30)

fig.suptitle("Tourism Development Programme: Baseline vs. NDPIV Targets",
             fontsize=13, fontweight="bold", y=1.01, color=DARK)
fig.tight_layout()
fig.text(0.5, -0.01,
         "Strategy: Phase 1 — 5× tourist inflows | Phase 2 — Double spend & stay per tourist",
         ha="center", fontsize=8.5, color=GRAY, style="italic")
save(fig, "07_tourism_results")

# ════════════════════════════════════════════════════════════════════════════
# 8. EXTRACTIVES Programme Results
# ════════════════════════════════════════════════════════════════════════════
print("Chart 8: Extractives Results")

ext_metrics = [
    "Petroleum Storage\nCapacity (mn litres)",
    "Oil & Gas Revenue\n(UGX bn)",
    "Ugandans Employed\nin Extractives (000s)",
    "Investment in\nMineral Value Add (USD bn)",
    "Investment in Oil\n& Gas Dev (USD bn)",
    "Programme\nPerformance (%)",
]
ext_base = [99.1, 62.98, 5,    0.8, 0.8, 65]
ext_tgt  = [150,  265,   50,   2.0, 2.0, 85]

fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.flatten()
for i, (lbl, b, t) in enumerate(zip(ext_metrics, ext_base, ext_tgt)):
    ax = axes[i]
    bars = ax.bar(["Baseline", "Target\n(NDPIV)"],
                  [b, t], color=[AMBER, TEAL], width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        fmt = f"{val:,.1f}" if val < 200 else f"{val:,.0f}"
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04, fmt,
                ha="center", fontsize=9.5, fontweight="bold",
                color=bar.get_facecolor())
    chg = ((t - b) / b * 100)
    ax.text(0.97, 0.93, f"▲ {chg:.0f}%",
            transform=ax.transAxes, ha="right", fontsize=9.5,
            color=TEAL, fontweight="bold")
    ax.set_title(lbl, fontsize=10, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.3)

fig.suptitle("Extractives Development Programme: Baseline vs. NDPIV Targets\n"
             "(Minerals incl. Oil & Gas)",
             fontsize=13, fontweight="bold", y=1.01, color=DARK)
fig.tight_layout()
save(fig, "08_extractives_results")

# ════════════════════════════════════════════════════════════════════════════
# 9. PRIVATE SECTOR DEVELOPMENT Results
# ════════════════════════════════════════════════════════════════════════════
print("Chart 9: Private Sector Results")

pvt_metrics = [
    "Average Business\nLifespan (years)",
    "Informal Sector\nSize (%)",
    "Value of Exports\n(USD bn)",
    "Public Contracts to\nLocal Firms (%)",
]
pvt_base = [6,    54.8, 7.9, 64]
pvt_tgt  = [10,   41.5, 10.3, 70]
pvt_lb   = {1}   # informal sector — lower is better

fig, axes = plt.subplots(1, 4, figsize=(16, 5))
for i, (lbl, b, t) in enumerate(zip(pvt_metrics, pvt_base, pvt_tgt)):
    ax = axes[i]
    lb = i in pvt_lb
    cols = ([AMBER, GREEN] if not lb else [GREEN, RED])
    bars = ax.bar(["Baseline\n(FY2023/24)", "Target\n(FY2029/30)"],
                  [b, t], color=cols, width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04, f"{val:.1f}",
                ha="center", fontsize=9.5, fontweight="bold",
                color=bar.get_facecolor())
    chg = ((t - b) / b * 100)
    sym = "▼" if lb else "▲"
    ax.text(0.97, 0.93, f"{sym} {abs(chg):.0f}%",
            transform=ax.transAxes, ha="right", fontsize=9.5,
            color=GREEN if not lb else RED, fontweight="bold")
    ax.set_title(lbl, fontsize=10, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.3)

fig.suptitle("Private Sector Development Programme: Baseline vs. NDPIV Targets",
             fontsize=13, fontweight="bold", y=1.04, color=DARK)
fig.tight_layout()
save(fig, "09_private_sector_results")

# ════════════════════════════════════════════════════════════════════════════
# 10. LENDING RATE REDUCTION TARGETS
# ════════════════════════════════════════════════════════════════════════════
print("Chart 10: Lending Rates")

lenders  = ["Commercial Banks", "Tier 4 Institutions", "Money Lenders", "DFIs (e.g. UDB)"]
lr_base  = [18.0, 48.0, 120.0, 12.0]
lr_tgt   = [14.9, 38.0,  60.0,  8.0]

fig, ax = plt.subplots(figsize=(11, 5.5))
x = np.arange(len(lenders)); w = 0.35
b1 = ax.bar(x - w/2, lr_base, w, color=RED,   label="Current Rate (FY2023/24)", zorder=3)
b2 = ax.bar(x + w/2, lr_tgt,  w, color=GREEN, label="Target Rate (FY2029/30)",  zorder=3, alpha=0.9)
ax.set_xticks(x); ax.set_xticklabels(lenders, fontsize=10)
ax.set_ylabel("Annual Interest Rate (%)", fontsize=10)
ax.set_title("Lending Rate Reduction Targets by Institution Type\n"
             "(Private Sector Development Programme — NDPIV)",
             fontsize=12, fontweight="bold", loc="left", color=DARK)
ax.legend(fontsize=10)

for bar, val in zip(b1, lr_base):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
            f"{val:.1f}%", ha="center", fontsize=9, fontweight="bold", color=RED)
for bar, val in zip(b2, lr_tgt):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
            f"{val:.1f}%", ha="center", fontsize=9, fontweight="bold", color=GREEN)

# Reduction arrows
for i, (b, t) in enumerate(zip(lr_base, lr_tgt)):
    reduction = b - t
    ax.text(i, max(b, t) * 1.05,
            f"−{reduction:.1f}pp", ha="center", fontsize=9,
            color=DARK, fontweight="bold")

ax.set_ylim(0, 145)
fig.text(0.5, -0.04,
         "pp = percentage points reduction | DFI = Development Finance Institutions",
         ha="center", fontsize=8, color=GRAY, style="italic")
save(fig, "10_lending_rates")

# ════════════════════════════════════════════════════════════════════════════
# 11. INNOVATION / STI Programme Results
# ════════════════════════════════════════════════════════════════════════════
print("Chart 11: STI Results")

sti_labels = [
    "Annual Govt + Private\nSTI Investment (USD mn)",
    "Innovation-Driven\nEnterprises Created",
    "IDEs with Export\nMarket Presence",
    "STI Contribution\nto GDP (USD bn)",
    "Productive STI\nHuman Capital (000s)",
]
sti_base = [50,  0,  0,  1,  50]   # approximate baseline
sti_tgt  = [500, 50, 10, 10, 500]

fig, axes = plt.subplots(1, 5, figsize=(18, 5.5))
for i, (lbl, b, t) in enumerate(zip(sti_labels, sti_base, sti_tgt)):
    ax = axes[i]
    bars = ax.bar(["Baseline", "Target"],
                  [b, t], color=[AMBER, PURPLE], width=0.45, zorder=3)
    for bar, val in zip(bars, [b, t]):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() * 1.04,
                f"{val:,}", ha="center", fontsize=9, fontweight="bold",
                color=bar.get_facecolor())
    ax.set_title(lbl, fontsize=8.5, fontweight="bold", color=DARK)
    ax.set_ylim(0, max(b, t) * 1.3)
    if b > 0:
        ax.text(0.97, 0.93, f"▲ {(t/b-1)*100:.0f}×" if t/b > 5 else f"▲ {(t-b)/b*100:.0f}%",
                transform=ax.transAxes, ha="right", fontsize=9,
                color=PURPLE, fontweight="bold")

fig.suptitle("Innovation, Technology & STI Programme: Targets (NDPIV)",
             fontsize=13, fontweight="bold", y=1.04, color=DARK)
fig.tight_layout()
fig.text(0.5, -0.03,
         "STI = Science, Technology & Innovation | IDEs = Innovation-Driven Enterprises",
         ha="center", fontsize=8, color=GRAY, style="italic")
save(fig, "11_sti_results")

# ════════════════════════════════════════════════════════════════════════════
# 12. ATMS STRATEGIC PRIORITY AREAS — Revenue Targets
# ════════════════════════════════════════════════════════════════════════════
print("Chart 12: ATMS Targets")

atms = ["Agro-based\nManufacturing", "Tourism\nInflows",
        "Mineral-based\nManufacturing\n(incl. Oil & Gas)", "STI / Knowledge\nEconomy\n(Multiplier)"]
atms_tgt = [20, 50, 25, None]   # USD billions
atms_cols = [GREEN, TEAL, AMBER, PURPLE]

fig, ax = plt.subplots(figsize=(11, 6))
bar_vals = [20, 50, 25, 5]   # STI shown as symbolic multiplier
bars = ax.bar(atms, bar_vals, color=atms_cols, width=0.5, zorder=3)
for bar, val, label in zip(bars, atms_tgt, ["USD 20bn+", "USD 50bn+", "USD 25bn+", "Multiplier\n(Unlocks All)"]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            label, ha="center", fontsize=11, fontweight="bold",
            color=bar.get_facecolor())

ax.set_ylabel("Target Revenue (USD Billions)", fontsize=10)
ax.set_title("ATMS: Strategic Priority Areas & Revenue Targets\n"
             "Combined target: USD 95bn+ — anchoring the 10-Fold Growth Strategy",
             fontsize=12, fontweight="bold", loc="left", color=DARK)
ax.set_ylim(0, 65)
ax.axhline(y=0, color=DARK, lw=0.5)

# Total annotation
ax.annotate("Combined ATMS\nRevenue Target:\nUSD 95bn+",
            xy=(2.5, 50), fontsize=11, color=DARK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor=LGRAY, edgecolor=DARK, lw=1.2))

fig.text(0.5, -0.03,
         "ATMS = Agro-industrialisation, Tourism, Minerals (incl. Oil & Gas), Science Technology & Innovation",
         ha="center", fontsize=8.5, color=GRAY, style="italic")
save(fig, "12_atms_targets")

# ════════════════════════════════════════════════════════════════════════════
# 13. ECONOMIC STRUCTURE SHIFT (Agriculture vs Industry share of GDP)
# ════════════════════════════════════════════════════════════════════════════
print("Chart 13: Economic Structure Shift")

sectors_gdp = ["Agriculture", "Industry", "Services\n& Other"]
gdp_2010    = [53.1, 9.5,  37.4]
gdp_2040    = [10.4, 31.4, 58.2]   # services = remainder

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
wedge_cols = [GREEN, NAVY, TEAL]

for ax, data, yr in zip(axes, [gdp_2010, gdp_2040], ["2010 (Baseline)", "2040 (Target)"]):
    wedges, texts, autos = ax.pie(
        data, labels=sectors_gdp, colors=wedge_cols,
        autopct="%1.1f%%", startangle=90,
        wedgeprops=dict(width=0.6, edgecolor="white", linewidth=2),
        pctdistance=0.78
    )
    for at in autos:
        at.set_fontsize(10); at.set_fontweight("bold")
    for txt in texts:
        txt.set_fontsize(10)
    ax.set_title(yr, fontsize=12, fontweight="bold", color=DARK, pad=12)

fig.suptitle("Economic Structure Transformation: GDP Composition\n"
             "Agriculture declining from 53.1% → 10.4% | Industry rising 9.5% → 31.4%",
             fontsize=13, fontweight="bold", y=1.02, color=DARK)
patches = [mpatches.Patch(color=c, label=l)
           for c, l in zip(wedge_cols, sectors_gdp)]
fig.legend(handles=patches, loc="lower center", ncol=3,
           fontsize=10, bbox_to_anchor=(0.5, -0.04))
fig.tight_layout()
save(fig, "13_economic_structure")

# ════════════════════════════════════════════════════════════════════════════
# 14. LABOUR FORCE SHIFT (Agriculture vs Industry)
# ════════════════════════════════════════════════════════════════════════════
print("Chart 14: Labour Force Shift")

labour_cats = ["Agriculture", "Industry", "Services\n& Other"]
lf_2010     = [65.6, 7.6,  26.8]
lf_2040     = [31.0, 26.0, 43.0]

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
lf_cols = [GREEN, NAVY, TEAL]

for ax, data, yr in zip(axes, [lf_2010, lf_2040], ["2010 (Baseline)", "2040 (Target)"]):
    wedges, texts, autos = ax.pie(
        data, labels=labour_cats, colors=lf_cols,
        autopct="%1.1f%%", startangle=90,
        wedgeprops=dict(width=0.6, edgecolor="white", linewidth=2),
        pctdistance=0.78
    )
    for at in autos:
        at.set_fontsize(10); at.set_fontweight("bold")
    for txt in texts:
        txt.set_fontsize(10)
    ax.set_title(yr, fontsize=12, fontweight="bold", color=DARK, pad=12)

fig.suptitle("Labour Force Transformation: Sector Employment Composition\n"
             "Agriculture falling from 65.6% → 31% | Industry rising from 7.6% → 26%",
             fontsize=13, fontweight="bold", y=1.02, color=DARK)
patches = [mpatches.Patch(color=c, label=l)
           for c, l in zip(lf_cols, labour_cats)]
fig.legend(handles=patches, loc="lower center", ncol=3,
           fontsize=10, bbox_to_anchor=(0.5, -0.04))
fig.tight_layout()
save(fig, "14_labour_force_shift")

# ════════════════════════════════════════════════════════════════════════════
# 15. SUMMARY DASHBOARD — All Key Metrics at a Glance
# ════════════════════════════════════════════════════════════════════════════
print("Chart 15: Summary Dashboard")

fig = plt.figure(figsize=(18, 14))
fig.patch.set_facecolor(WHITE)

# Title bar
ax_title = fig.add_axes([0, 0.94, 1, 0.06])
ax_title.set_facecolor(NAVY); ax_title.axis("off")
ax_title.text(0.5, 0.55,
    "Uganda 10-Fold Growth Strategy — Key Metrics Dashboard | NPA Kyankwanzi April 2026",
    ha="center", va="center", fontsize=15, fontweight="bold", color=WHITE,
    transform=ax_title.transAxes)

# KPI cards row
kpi_data = [
    ("Current GDP",        "USD 60bn",     "(FY2024/25)",    NAVY),
    ("10-Fold Target",     "USD 600bn",    "(by 2040)",      GREEN),
    ("NDPIV GDP Target",   "USD 158bn",    "(by FY2029/30)", TEAL),
    ("Annual Jobs Target", "885,000",      "per year",       AMBER),
    ("Tourism Target",     "USD 10bn",     "forex earnings", PURPLE),
    ("Poverty Reduction",  "16.9% → 12.9%","by 2029/30",    GOLD),
]
for i, (lbl, val, sub, col) in enumerate(kpi_data):
    ax = fig.add_axes([0.005 + i*0.166, 0.82, 0.155, 0.105])
    ax.set_facecolor(LGRAY); ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0.88), 1, 0.12, color=col,
                                transform=ax.transAxes, clip_on=False))
    ax.text(0.5, 0.62, val,  ha="center", va="center", fontsize=13,
            fontweight="bold", color=col, transform=ax.transAxes)
    ax.text(0.5, 0.38, lbl,  ha="center", va="center", fontsize=8,
            color=GRAY, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, 0.18, sub,  ha="center", va="center", fontsize=7.5,
            color=GRAY, transform=ax.transAxes)

# ── Sub-chart A: GDP Trajectory (left) ─────────────────────────────────────
ax_a = fig.add_axes([0.04, 0.52, 0.42, 0.27])
years2 = [2010, 2015, 2020, 2025, 2030, 2035, 2040]
hist   = [17,   26,   38,   60,   None, None, None]
fold   = [None, None, None, 60,   158,  350,  600]
base   = [None, None, None, 60,   84,   118,  166]
ax_a.plot([y for y, v in zip(years2, hist)  if v], [v for v in hist  if v],
          color=NAVY,  lw=2.5, marker="o", ms=5, label="Historical")
ax_a.plot([y for y, v in zip(years2, base)  if v], [v for v in base  if v],
          color=GRAY,  lw=1.8, ls="--", label="7% baseline")
ax_a.plot([y for y, v in zip(years2, fold)  if v], [v for v in fold  if v],
          color=GREEN, lw=2.5, marker="^", ms=5, label="10-Fold target")
ax_a.set_title("GDP Trajectory (USD bn)", fontsize=10, fontweight="bold", color=DARK)
ax_a.legend(fontsize=7.5); ax_a.set_ylim(0, 680)
ax_a.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}bn"))

# ── Sub-chart B: ATMS Targets (right) ─────────────────────────────────────
ax_b = fig.add_axes([0.55, 0.52, 0.42, 0.27])
atms_lbl = ["Agro-Mfg\n(USD 20bn+)", "Tourism\n(USD 50bn+)",
            "Minerals\n(USD 25bn+)", "STI\n(Multiplier)"]
atms_v   = [20, 50, 25, 5]
ax_b.bar(atms_lbl, atms_v, color=[GREEN, TEAL, AMBER, PURPLE], zorder=3, width=0.5)
for i, (lbl, v) in enumerate(zip(["$20bn+","$50bn+","$25bn+","Multiplier"], atms_v)):
    ax_b.text(i, v + 0.5, lbl, ha="center", fontsize=9, fontweight="bold")
ax_b.set_title("ATMS Revenue Targets (USD bn)", fontsize=10, fontweight="bold", color=DARK)
ax_b.set_ylim(0, 65)

# ── Sub-chart C: Sector Structure (bottom left) ────────────────────────────
ax_c = fig.add_axes([0.04, 0.06, 0.27, 0.40])
x_s = np.arange(3); w_s = 0.35
labels_s = ["Agriculture", "Industry", "Services"]
ax_c.bar(x_s - w_s/2, gdp_2010, w_s, color=[GREEN, NAVY, TEAL], label="2010", zorder=3)
ax_c.bar(x_s + w_s/2, gdp_2040, w_s, color=[GREEN, NAVY, TEAL], label="2040",
         zorder=3, alpha=0.55, hatch="//")
ax_c.set_xticks(x_s); ax_c.set_xticklabels(labels_s, fontsize=9)
ax_c.set_ylabel("% of GDP", fontsize=9)
ax_c.set_title("GDP Sector Composition (%)", fontsize=10, fontweight="bold", color=DARK)
ax_c.legend(fontsize=8.5)

# ── Sub-chart D: Labour Force (bottom centre) ──────────────────────────────
ax_d = fig.add_axes([0.37, 0.06, 0.27, 0.40])
ax_d.bar(x_s - w_s/2, lf_2010, w_s, color=[GREEN, NAVY, TEAL], label="2010", zorder=3)
ax_d.bar(x_s + w_s/2, lf_2040, w_s, color=[GREEN, NAVY, TEAL], label="2040",
         zorder=3, alpha=0.55, hatch="//")
ax_d.set_xticks(x_s); ax_d.set_xticklabels(labels_s, fontsize=9)
ax_d.set_ylabel("% of Labour Force", fontsize=9)
ax_d.set_title("Labour Force Composition (%)", fontsize=10, fontweight="bold", color=DARK)
ax_d.legend(fontsize=8.5)

# ── Sub-chart E: NDPIV Macro targets (bottom right) ───────────────────────
ax_e = fig.add_axes([0.70, 0.06, 0.27, 0.40])
macro_lbls_s = ["Poverty (%)", "GDP Growth (%)", "Revenue/GDP (%)"]
macro_b_s    = [16.9, 5.5, 14.0]
macro_t_s    = [12.9, 10.1, 18.3]
x_m = np.arange(3); w_m = 0.35
b1 = ax_e.bar(x_m - w_m/2, macro_b_s, w_m, color=AMBER,  label="Current", zorder=3)
b2 = ax_e.bar(x_m + w_m/2, macro_t_s, w_m, color=GREEN, label="NDPIV Target", zorder=3, alpha=0.9)
ax_e.set_xticks(x_m); ax_e.set_xticklabels(macro_lbls_s, fontsize=8.5)
ax_e.set_ylabel("Value (%)", fontsize=9)
ax_e.set_title("NDPIV Key Macro Targets", fontsize=10, fontweight="bold", color=DARK)
ax_e.legend(fontsize=8.5)

fig.text(0.5, 0.01,
    "Source: NPA Presentation — NRM MPs Retreat, Kyankwanzi April 2026 | Vision 2040 | NDPIV",
    ha="center", fontsize=8.5, color=GRAY, style="italic")

save(fig, "15_summary_dashboard")

print(f"\n✅  All 15 charts saved to '{OUT}/' folder.")
print("    Run: pip install matplotlib numpy pandas")
print("    Then: python npa_ndpiv_visualizations.py")
