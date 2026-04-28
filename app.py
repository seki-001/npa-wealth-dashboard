import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

# --- Page configuration ---
st.set_page_config(page_title="Uganda 10-Fold Growth Dashboard", layout="wide", page_icon="🇺🇬")

# --- Custom CSS for Screenshot UI Match ---
st.markdown("""
<style>
    /* Main Background */
    .stApp { background-color: #f3f4f6; }
    
    /* KPI Cards */
    .kpi-card {
        background-color: white;
        border-radius: 8px;
        padding: 15px 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        border-top: 4px solid #0F3460;
        height: 100%;
        margin-bottom: 1rem;
    }
    .kpi-value {
        font-size: 26px;
        font-weight: 800;
        margin: 5px 0;
    }
    .kpi-label {
        font-size: 11px;
        color: #6B7280;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .kpi-sub {
        font-size: 11px;
        color: #9CA3AF;
    }
    
    /* Title Customization */
    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .sub-title {
        font-size: 14px;
        font-weight: 600;
        color: #4b5563;
        margin-top: 5px;
        margin-bottom: 25px;
    }
    
    /* Sidebar styling */
    .sidebar-heading {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }
    .sidebar-sub {
        font-size: 13px;
        color: #4b5563;
        margin-bottom: 15px;
    }
    .stDownloadButton button {
        width: 100%;
        background-color: white;
        border: 1px solid #d1d5db;
        color: #374151;
    }
    .stDownloadButton button:hover {
        border-color: #1B6B3A;
        color: #1B6B3A;
    }
</style>
""", unsafe_allow_html=True)

# --- Color Palette ---
COLORS = {
    "NAVY": "#0F3460", "GREEN": "#1B6B3A", "AMBER": "#B45309", 
    "TEAL": "#0E7490", "PURPLE": "#6D28D9", "GOLD": "#CA8A04", 
    "RED": "#B91C1C", "GRAY": "#6B7280", "DARK": "#16213E"
}

# ════════════════════════════════════════════════════════════════════════════
# DATA DEFINITIONS (for both UI and Export)
# ════════════════════════════════════════════════════════════════════════════

# 1. Macro Targets
df_macro = pd.DataFrame({
    "Indicator": ["Poverty Rate (%)", "GDP Growth (%)", "Per Capita (USD)", "Jobs Created (000s)", "Inflation (%)", "Revenue/GDP (%)"] * 2,
    "Value": [16.9, 5.5, 1154, 500, 5.0, 14.0] + [12.9, 10.1, 2942, 885, 5.0, 18.3],
    "Period": ["Current (FY2024/25)"] * 6 + ["Target (FY2029/30)"] * 6
})

# 2. Vision 2040 Targets
metrics = ["GDP (USD bn)", "Per Capita Income (USD)", "Population Below Poverty (%)", 
           "Agriculture % of GDP", "Industry % of GDP", "Manufactured Goods in Exports (%)",
           "Agri Labour Force (%)", "Industry Labour Force (%)", "Patents Registered/yr"]
baseline = [17, 506, 24.5, 53.1, 9.5, 4.2, 65.6, 7.6, 3]
target = [580.5, 9500, 5, 10.4, 31.4, 50, 31, 26, 6000]

df_vision = pd.DataFrame({
    "Indicator": metrics,
    "Baseline_2010": baseline,
    "Target_2040": target
})

# 3. GDP Trajectory
df_gdp_traj = pd.DataFrame({
    "Year": [2010, 2015, 2020, 2022, 2025, 2030, 2035, 2040],
    "Historical": [17, 26, 38, 47, 60, None, None, None],
    "Baseline_7pct": [None, None, None, None, 60, 84, 118, 166],
    "Target_10Fold": [None, None, None, None, 60, 158, 350, 600]
})

# 4. Economic Structure & Labour
df_struct = pd.DataFrame({
    "Sector": ["Agriculture", "Industry", "Services & Other"],
    "GDP_2010_pct": [53.1, 9.5, 37.4],
    "GDP_2040_pct": [10.4, 31.4, 58.2],
    "Labour_2010_pct": [65.6, 7.6, 26.8],
    "Labour_2040_pct": [31.0, 26.0, 43.0]
})

# 5. Sector Programmes
prog_data = []
prog_data.extend([("Agro-Industrialisation", ind, b, t) for ind, b, t in zip(
    ["Agri Growth Rate (%)", "Export Value (USD mn)", "Import Value (USD mn)", "Food Security (%)", "Agri Financing Share (%)", "Annual Jobs (000s)"],
    [5.1, 2500, 1096, 71, 11.3, 0], [8.0, 4800, 600, 85, 15.0, 60])])
prog_data.extend([("Tourism Development", ind, b, t) for ind, b, t in zip(
    ["Forex Earnings (USD bn)", "Length of Stay (nights)", "Spend per Tourist (USD)", "Satisfaction Score (%)", "Domestic Exp (UGX bn)", "Programme Perf (%)"],
    [1.0, 7.6, 1550, 79, 3675, 57.7], [10.0, 14.0, 3100, 85, 7350, 70.0])])
prog_data.extend([("Extractives Industry", ind, b, t) for ind, b, t in zip(
    ["Storage Capacity (mn L)", "Oil/Gas Revenue (UGX bn)", "Ugandans Employed (000s)", "Mineral Value Add Inv (USD bn)", "Oil/Gas Dev Inv (USD bn)", "Programme Perf (%)"],
    [99.1, 62.98, 5, 0.8, 0.8, 65], [150, 265, 50, 2.0, 2.0, 85])])
prog_data.extend([("Private Sector Development", ind, b, t) for ind, b, t in zip(
    ["Business Lifespan (yrs)", "Informal Sector Size (%)", "Export Value (USD bn)", "Public Contracts to Locals (%)"],
    [6, 54.8, 7.9, 64], [10, 41.5, 10.3, 70])])
prog_data.extend([("Innovation / STI", ind, b, t) for ind, b, t in zip(
    ["STI Investment (USD mn)", "IDEs Created", "IDEs with Export Market", "STI GDP Contrib (USD bn)", "STI Human Capital (000s)"],
    [50, 0, 0, 1, 50], [500, 50, 10, 10, 500])])
df_programmes = pd.DataFrame(prog_data, columns=["Programme", "Indicator", "Baseline", "Target"])

# 6. ATMS Revenue Targets
df_atms = pd.DataFrame({
    "Sector": ["Agro-based Manufacturing", "Tourism Inflows", "Mineral-based Mfg (incl. Oil & Gas)", "STI / Knowledge Economy"],
    "Revenue_bn": [20, 50, 25, 5],
    "Label": ["USD 20bn+", "USD 50bn+", "USD 25bn+", "Multiplier"]
})

# 7. Lending Rates
df_rates = pd.DataFrame({
    "Institution": ["Commercial Banks", "Tier 4 Inst", "Money Lenders", "DFIs (e.g. UDB)"],
    "Current_Rate": [18.0, 48.0, 120.0, 12.0],
    "Target_Rate": [14.9, 38.0, 60.0, 8.0]
})

# 8. High-Impact Projects
df_projects = pd.DataFrame({
    "Priority_Area": ["Integrated Transport", "Sustainable Energy", "Human Capital", 
                      "Knowledge Economy (STI)", "Sustainable Extractives", "Agro-Industrialisation", 
                      "Cultural & Sports", "Urban & Housing", "Tourism Dev", 
                      "Private Sector Dev", "Monetization of Economy", "Manufacturing"],
    "Projects_Count": [15, 13, 9, 6, 5, 4, 3, 2, 3, 1, 1, 1]
})

# 9. Timeline
df_timeline = pd.DataFrame([
    dict(Task="NDP I", Start="2010-07-01", Finish="2015-06-30", Status="Completed"),
    dict(Task="NDP II", Start="2015-07-01", Finish="2020-06-30", Status="Completed"),
    dict(Task="NDP III", Start="2020-07-01", Finish="2025-06-30", Status="Running"),
    dict(Task="NDP IV", Start="2025-07-01", Finish="2030-06-30", Status="Running"),
    dict(Task="NDP V", Start="2030-07-01", Finish="2035-06-30", Status="Not Yet"),
    dict(Task="NDP VI", Start="2035-07-01", Finish="2040-06-30", Status="Not Yet")
])

# --- Helpers ---
def apply_chart_layout(fig):
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=40, b=20), title_font_color=COLORS['DARK']
    )
    fig.update_xaxes(showgrid=False, linecolor='#CBD5E1')
    fig.update_yaxes(showgrid=True, gridcolor='#E5E7EB', linecolor='#CBD5E1')
    return fig

@st.cache_data
def generate_excel():
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_macro.to_excel(writer, sheet_name='Macro Targets', index=False)
        df_vision.to_excel(writer, sheet_name='Vision 2040', index=False)
        df_gdp_traj.to_excel(writer, sheet_name='GDP Trajectory', index=False)
        df_struct.to_excel(writer, sheet_name='Economic Shift', index=False)
        df_programmes.to_excel(writer, sheet_name='Sector Programmes', index=False)
        df_atms.to_excel(writer, sheet_name='ATMS Targets', index=False)
        df_rates.to_excel(writer, sheet_name='Lending Rates', index=False)
        df_projects.to_excel(writer, sheet_name='High Impact Projects', index=False)
    return output.getvalue()

@st.cache_data
def generate_csv():
    # Merge key datasets for CSV
    df_concat = pd.concat([
        df_macro.rename(columns={"Period": "Detail"}),
        df_programmes.melt(id_vars=["Programme", "Indicator"], var_name="Detail", value_name="Value").rename(columns={"Programme": "Category"})
    ], ignore_index=True)
    return df_concat.to_csv(index=False).encode('utf-8')


# ════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════════════════
st.sidebar.markdown('<div class="sidebar-heading">Filters</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-sub">Use these slicers to filter the Executive Summary and Programme Details.</div>', unsafe_allow_html=True)

all_programmes = df_programmes["Programme"].unique().tolist()
selected_progs = st.sidebar.multiselect("Select Programme(s)", all_programmes, default=all_programmes)

st.sidebar.markdown("<br><hr>", unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-heading">📥 Export Data</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-sub">Download the reports for offline analysis.</div>', unsafe_allow_html=True)

st.sidebar.download_button(
    label="📄 Download Filtered Data (CSV)",
    data=generate_csv(),
    file_name="npa_10fold_growth_data.csv",
    mime="text/csv"
)

st.sidebar.download_button(
    label="📊 Download Full Report (Excel)",
    data=generate_excel(),
    file_name="NPA_10Fold_Growth_Report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


# ════════════════════════════════════════════════════════════════════════════
# MAIN AREA
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="main-title">Uganda\'s 10-Fold Growth Strategy 🔗</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Executive Dashboard | NPA Overview, April 2026 | Vision 2040 Targets</div>', unsafe_allow_html=True)

# --- KPI Row ---
def create_kpi(label, value, sub, color):
    return f"""
    <div class="kpi-card" style="border-top-color: {color};">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value" style="color: {color};">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """

c1, c2, c3, c4 = st.columns(4)
c1.markdown(create_kpi("10-Fold GDP Target", "USD 600bn", "By 2040 (Vision 2040)", COLORS["NAVY"]), unsafe_allow_html=True)
c2.markdown(create_kpi("Annual Jobs Target", "885,000", "Per year by FY 2029/30", COLORS["GREEN"]), unsafe_allow_html=True)
c3.markdown(create_kpi("Poverty Target", "12.9%", "Down from 16.9% by 2029/30", COLORS["AMBER"]), unsafe_allow_html=True)
c4.markdown(create_kpi("ATMS Combined Target", "USD 95bn+", "Annual anchoring revenue", COLORS["PURPLE"]), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs([
    "Executive Summary",
    "Programme Details",
    "Macro & Survey Insights"
])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### GDP Trajectory: Historical vs 10-Fold Strategy")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_gdp_traj["Year"], y=df_gdp_traj["Historical"], mode='lines+markers', name='Historical GDP', line=dict(color=COLORS['NAVY'], width=3), marker=dict(size=8)))
        fig1.add_trace(go.Scatter(x=df_gdp_traj["Year"], y=df_gdp_traj["Baseline_7pct"], mode='lines+markers', name='7% Baseline Growth', line=dict(color=COLORS['GRAY'], width=2, dash='dash')))
        fig1.add_trace(go.Scatter(x=df_gdp_traj["Year"], y=df_gdp_traj["Target_10Fold"], mode='lines+markers', name='10-Fold Growth Target', line=dict(color=COLORS['GREEN'], width=3), marker=dict(symbol='triangle-up', size=10)))
        fig1.update_layout(yaxis_title="GDP (USD Billions)", yaxis=dict(tickprefix="$", ticksuffix="bn"))
        st.plotly_chart(apply_chart_layout(fig1), use_container_width=True)

    with col2:
        st.markdown("#### NDPIV Macro Outlook Targets (FY2029/30)")
        fig2 = px.bar(df_macro, x="Indicator", y="Value", color="Period", barmode="group", text="Value",
                      color_discrete_map={"Current (FY2024/25)": COLORS["AMBER"], "Target (FY2029/30)": COLORS["GREEN"]})
        fig2.update_traces(textposition='outside')
        fig2.update_layout(yaxis_title="Value", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(apply_chart_layout(fig2), use_container_width=True)

    st.markdown("---")
    
    st.markdown("#### Vision 2040 Targets: Baseline (2010) vs 2040 Goals")
    # Display the 9 Vision 2040 metrics
    rows = [st.columns(3) for _ in range(3)]
    for i, row in df_vision.iterrows():
        col = rows[i // 3][i % 3]
        with col:
            m = row["Indicator"]
            b = row["Baseline_2010"]
            t = row["Target_2040"]
            df_v = pd.DataFrame({"Period": ["Baseline (2010)", "Target (2040)"], "Value": [b, t]})
            lower_is_better = m in ["Population Below Poverty (%)", "Agriculture % of GDP", "Agri Labour Force (%)"]
            
            c1 = COLORS["AMBER"] if not lower_is_better else COLORS["GREEN"]
            c2 = COLORS["GREEN"] if not lower_is_better else COLORS["RED"]
            
            fig_v = px.bar(df_v, x="Period", y="Value", text="Value", color="Period",
                           color_discrete_map={"Baseline (2010)": c1, "Target (2040)": c2})
            fig_v.update_traces(textposition='outside')
            fig_v.update_layout(title=m, title_font_size=13, showlegend=False, height=250, margin=dict(t=30, b=0, l=0, r=0))
            st.plotly_chart(apply_chart_layout(fig_v), use_container_width=True)
            
    st.markdown("---")
    st.markdown("#### NDP Timeline (2010 - 2040)")
    color_map = {"Completed": COLORS['GREEN'], "Running": COLORS['AMBER'], "Not Yet": COLORS['GRAY']}
    fig9 = px.timeline(df_timeline, x_start="Start", x_end="Finish", y="Task", color="Status", color_discrete_map=color_map)
    fig9.update_yaxes(autorange="reversed")
    fig9.update_layout(height=300)
    st.plotly_chart(apply_chart_layout(fig9), use_container_width=True)


with tab2:
    st.markdown("#### Sector Programmes")
    st.info("💡 Data in this section is filtered by the Programme(s) Slicer in the sidebar.")
    
    if selected_progs:
        filtered_df = df_programmes[df_programmes["Programme"].isin(selected_progs)]
        for prog in selected_progs:
            prog_df = filtered_df[filtered_df["Programme"] == prog]
            df_melt = prog_df.melt(id_vars=["Indicator"], value_vars=["Baseline", "Target"], var_name="Period", value_name="Value")
            
            st.markdown(f"**{prog}**")
            fig3 = px.bar(df_melt, x="Indicator", y="Value", color="Period", barmode="group", text="Value",
                          color_discrete_map={"Baseline": COLORS["AMBER"], "Target": COLORS["GREEN"]})
            fig3.update_traces(textposition='outside')
            fig3.update_layout(height=350, margin=dict(t=10, b=10))
            st.plotly_chart(apply_chart_layout(fig3), use_container_width=True)
            st.markdown("---")
    else:
        st.warning("Please select at least one programme from the sidebar.")
        
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("#### NDPIV High-Impact Projects")
        df_p_sorted = df_projects.sort_values("Projects_Count", ascending=True)
        fig8 = go.Figure(go.Bar(x=df_p_sorted["Projects_Count"], y=df_p_sorted["Priority_Area"], orientation='h', marker_color=COLORS['TEAL'], text=df_p_sorted["Projects_Count"], textposition='outside'))
        fig8.update_layout(height=450, margin=dict(l=0, r=0, t=10, b=10))
        st.plotly_chart(apply_chart_layout(fig8), use_container_width=True)
        
    with col4:
        st.markdown("#### Lending Rate Reduction Targets")
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(x=df_rates["Institution"], y=df_rates["Current_Rate"], name='Current (FY23/24)', marker_color=COLORS['RED']))
        fig7.add_trace(go.Bar(x=df_rates["Institution"], y=df_rates["Target_Rate"], name='Target (FY29/30)', marker_color=COLORS['GREEN']))
        fig7.update_layout(barmode='group', yaxis_title="Interest Rate (%)")
        st.plotly_chart(apply_chart_layout(fig7), use_container_width=True)


with tab3:
    st.markdown("#### Macro Context & Structural Transformation")
    st.info("💡 Data in this section represents national targets and is not filtered by the Slicer.")
    
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("**Economic Structure Shift (GDP %)**")
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=df_struct["Sector"], y=df_struct["GDP_2010_pct"], name='2010 (Baseline)', marker_color=COLORS['NAVY']))
        fig4.add_trace(go.Bar(x=df_struct["Sector"], y=df_struct["GDP_2040_pct"], name='2040 (Target)', marker_color=COLORS['GREEN']))
        fig4.update_layout(barmode='group')
        st.plotly_chart(apply_chart_layout(fig4), use_container_width=True)

    with col6:
        st.markdown("**Labour Force Shift (%)**")
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(x=df_struct["Sector"], y=df_struct["Labour_2010_pct"], name='2010 (Baseline)', marker_color=COLORS['NAVY']))
        fig5.add_trace(go.Bar(x=df_struct["Sector"], y=df_struct["Labour_2040_pct"], name='2040 (Target)', marker_color=COLORS['GREEN']))
        fig5.update_layout(barmode='group')
        st.plotly_chart(apply_chart_layout(fig5), use_container_width=True)

    st.markdown("---")
    
    st.markdown("#### ATMS: Strategic Priority Areas & Revenue Targets")
    st.markdown("*Combined target: USD 95bn+ — anchoring the 10-Fold Growth Strategy*")
    fig10 = go.Figure(data=[
        go.Bar(x=df_atms["Sector"], y=df_atms["Revenue_bn"], text=df_atms["Label"], textposition='outside',
               marker_color=[COLORS["GREEN"], COLORS["TEAL"], COLORS["AMBER"], COLORS["PURPLE"]])
    ])
    fig10.update_layout(yaxis_title="Target Revenue (USD Billions)", height=450)
    st.plotly_chart(apply_chart_layout(fig10), use_container_width=True)
