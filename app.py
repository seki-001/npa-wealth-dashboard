import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- Page configuration ---
st.set_page_config(page_title="Uganda 10-Fold Growth Dashboard", layout="wide", page_icon="🇺🇬")

# --- Custom CSS for Premium Power BI Look ---
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
        border-left: 5px solid #1B6B3A;
        height: 100%;
        margin-bottom: 1rem;
    }
    .kpi-value {
        font-size: 26px;
        font-weight: 800;
        color: #0F3460;
        margin: 5px 0;
    }
    .kpi-label {
        font-size: 13px;
        color: #6B7280;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .kpi-sub {
        font-size: 12px;
        color: #9CA3AF;
    }
    /* Headers */
    h1, h2, h3 { color: #111827; }
</style>
""", unsafe_allow_html=True)

# --- Color Palette ---
COLORS = {
    "NAVY": "#0F3460", "DARK": "#16213E", "GREEN": "#1B6B3A", 
    "AMBER": "#B45309", "RED": "#B91C1C", "TEAL": "#0E7490", 
    "PURPLE": "#6D28D9", "OLIVE": "#4D7C0F", "GRAY": "#6B7280", 
    "GOLD": "#CA8A04", "LGRAY": "#F1F5F9"
}

# --- Sidebar ---
st.sidebar.markdown("### 🇺🇬 10-Fold Growth Strategy")
st.sidebar.markdown("**National Planning Authority**<br>Kyankwanzi, April 2026", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("Navigate through the tabs in the main window to explore the targets and trajectories.")

# --- Main Title ---
st.title("Achieving Higher Middle-Income Status for Uganda")
st.markdown("##### The NRM Government's Strategy for 10-Fold Growth")
st.markdown("<br>", unsafe_allow_html=True)

# --- Helpers ---
def create_kpi(label, value, sub, color):
    return f"""
    <div class="kpi-card" style="border-left-color: {color};">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value" style="color: {color};">{value}</div>
        <div class="kpi-sub">{sub}</div>
    </div>
    """

def apply_chart_layout(fig):
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=40, b=20),
        title_font_color=COLORS['DARK']
    )
    fig.update_xaxes(showgrid=False, linecolor='#CBD5E1')
    fig.update_yaxes(showgrid=True, gridcolor='#E5E7EB', linecolor='#CBD5E1')
    return fig

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview & Macro",
    "🔄 Economic Transformation",
    "🏭 Sector Programmes",
    "📅 Timeline & Projects"
])

# ════════════════════════════════════════════════════════════════════════════
# TAB 1: Overview & Macro
# ════════════════════════════════════════════════════════════════════════════
with tab1:
    # --- KPI Row ---
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.markdown(create_kpi("Current GDP", "USD 60bn", "(FY2024/25)", COLORS["NAVY"]), unsafe_allow_html=True)
    c2.markdown(create_kpi("10-Fold Target", "USD 600bn", "(by 2040)", COLORS["GREEN"]), unsafe_allow_html=True)
    c3.markdown(create_kpi("NDPIV GDP", "USD 158bn", "(by FY2029/30)", COLORS["TEAL"]), unsafe_allow_html=True)
    c4.markdown(create_kpi("Annual Jobs", "885,000", "per year", COLORS["AMBER"]), unsafe_allow_html=True)
    c5.markdown(create_kpi("Tourism", "USD 10bn", "forex earnings", COLORS["PURPLE"]), unsafe_allow_html=True)
    c6.markdown(create_kpi("Poverty Rate", "16.9% → 12.9%", "by 2029/30", COLORS["GOLD"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### GDP Trajectory: Historical vs 10-Fold Strategy")
        years = [2010, 2015, 2020, 2022, 2025, 2030, 2035, 2040]
        gdp_actual = [17, 26, 38, 47, 60, None, None, None]
        gdp_baseline = [None, None, None, None, 60, 84, 118, 166]
        gdp_10fold = [None, None, None, None, 60, 158, 350, 600]
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=years, y=gdp_actual, mode='lines+markers', name='Historical GDP', line=dict(color=COLORS['NAVY'], width=3), marker=dict(size=8)))
        fig1.add_trace(go.Scatter(x=years, y=gdp_baseline, mode='lines+markers', name='7% Baseline Growth', line=dict(color=COLORS['GRAY'], width=2, dash='dash')))
        fig1.add_trace(go.Scatter(x=years, y=gdp_10fold, mode='lines+markers', name='10-Fold Growth Target', line=dict(color=COLORS['GREEN'], width=3), marker=dict(symbol='triangle-up', size=10)))
        
        # Annotations
        fig1.add_annotation(x=2040, y=600, text="10-Fold Target<br>USD 600bn", showarrow=True, arrowhead=1, arrowcolor=COLORS['GREEN'])
        fig1.add_annotation(x=2030, y=158, text="NDPIV Target<br>USD 158bn", showarrow=True, arrowhead=1, arrowcolor=COLORS['TEAL'])
        fig1.add_annotation(x=2025, y=60, text="Current<br>USD 60bn", showarrow=True, arrowhead=1, arrowcolor=COLORS['NAVY'])

        fig1.update_layout(yaxis_title="GDP (USD Billions)", yaxis=dict(tickprefix="$", ticksuffix="bn"))
        fig1 = apply_chart_layout(fig1)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("#### NDPIV Macro Outlook Targets (FY2029/30)")
        macro_labels = ["Poverty Rate (%)", "GDP Growth (%)", "Per Capita (USD)", "Jobs Created (000s)", "Inflation (%)", "Revenue/GDP (%)"]
        macro_baseline = [16.9, 5.5, 1154, 500, 5.0, 14.0]
        macro_target = [12.9, 10.1, 2942, 885, 5.0, 18.3]
        
        df_macro = pd.DataFrame({
            "Indicator": macro_labels * 2,
            "Value": macro_baseline + macro_target,
            "Period": ["Current (FY2024/25)"] * 6 + ["Target (FY2029/30)"] * 6
        })
        
        fig2 = px.bar(df_macro, x="Indicator", y="Value", color="Period", barmode="group", text="Value",
                      color_discrete_map={"Current (FY2024/25)": COLORS["AMBER"], "Target (FY2029/30)": COLORS["GREEN"]})
        fig2.update_traces(textposition='outside')
        fig2.update_layout(yaxis_title="Value", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        fig2 = apply_chart_layout(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Vision 2040 Targets: Baseline (2010) vs 2040 Goals")
    
    metrics = ["GDP (USD bn)", "Per Capita Income (USD)", "Population Below Poverty (%)", 
               "Agriculture % of GDP", "Industry % of GDP", "Manufactured Goods in Exports (%)",
               "Agri Labour Force (%)", "Industry Labour Force (%)", "Patents Registered/yr"]
    baseline = [17, 506, 24.5, 53.1, 9.5, 4.2, 65.6, 7.6, 3]
    target = [580.5, 9500, 5, 10.4, 31.4, 50, 31, 26, 6000]
    
    # Create 3x3 layout
    rows = [st.columns(3) for _ in range(3)]
    for i, (m, b, t) in enumerate(zip(metrics, baseline, target)):
        col = rows[i // 3][i % 3]
        with col:
            df_v = pd.DataFrame({"Period": ["Baseline (2010)", "Target (2040)"], "Value": [b, t]})
            lower_is_better = m in ["Population Below Poverty (%)", "Agriculture % of GDP", "Agri Labour Force (%)"]
            
            c1 = COLORS["AMBER"] if not lower_is_better else COLORS["GREEN"]
            c2 = COLORS["GREEN"] if not lower_is_better else COLORS["RED"]
            
            fig_v = px.bar(df_v, x="Period", y="Value", text="Value", color="Period",
                           color_discrete_map={"Baseline (2010)": c1, "Target (2040)": c2})
            fig_v.update_traces(textposition='outside')
            fig_v.update_layout(title=m, title_font_size=13, showlegend=False, height=250, margin=dict(t=30, b=0, l=0, r=0))
            fig_v = apply_chart_layout(fig_v)
            st.plotly_chart(fig_v, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 2: Economic Transformation
# ════════════════════════════════════════════════════════════════════════════
with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Economic Structure Shift")
        sectors_gdp = ["Agriculture", "Industry", "Services & Other"]
        gdp_2010 = [53.1, 9.5, 37.4]
        gdp_2040 = [10.4, 31.4, 58.2]
        
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=sectors_gdp, y=gdp_2010, name='2010 (Baseline)', marker_color=COLORS['NAVY']))
        fig3.add_trace(go.Bar(x=sectors_gdp, y=gdp_2040, name='2040 (Target)', marker_color=COLORS['GREEN']))
        
        fig3.update_layout(barmode='group', title="GDP Composition (%)", yaxis_title="% of GDP")
        fig3 = apply_chart_layout(fig3)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.markdown("#### Labour Force Shift")
        lf_2010 = [65.6, 7.6, 26.8]
        lf_2040 = [31.0, 26.0, 43.0]
        
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=sectors_gdp, y=lf_2010, name='2010 (Baseline)', marker_color=COLORS['NAVY']))
        fig4.add_trace(go.Bar(x=sectors_gdp, y=lf_2040, name='2040 (Target)', marker_color=COLORS['GREEN']))
        
        fig4.update_layout(barmode='group', title="Sector Employment Composition (%)", yaxis_title="% of Labour Force")
        fig4 = apply_chart_layout(fig4)
        st.plotly_chart(fig4, use_container_width=True)
        
    st.markdown("---")
    
    st.markdown("#### ATMS: Strategic Priority Areas & Revenue Targets")
    st.markdown("*Combined target: USD 95bn+ — anchoring the 10-Fold Growth Strategy*")
    
    atms = ["Agro-based Manufacturing", "Tourism Inflows", "Mineral-based Mfg (incl. Oil & Gas)", "STI / Knowledge Economy"]
    atms_vals = [20, 50, 25, 5]
    atms_text = ["USD 20bn+", "USD 50bn+", "USD 25bn+", "Multiplier (Unlocks All)"]
    
    fig5 = go.Figure(data=[
        go.Bar(x=atms, y=atms_vals, text=atms_text, textposition='outside',
               marker_color=[COLORS["GREEN"], COLORS["TEAL"], COLORS["AMBER"], COLORS["PURPLE"]])
    ])
    fig5.update_layout(yaxis_title="Target Revenue (USD Billions)", height=450)
    fig5 = apply_chart_layout(fig5)
    st.plotly_chart(fig5, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 3: Sector Programmes
# ════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("Select a programme to view results and targets:")
    programme = st.selectbox("", [
        "Agro-Industrialisation", 
        "Tourism Development", 
        "Extractives Industry", 
        "Private Sector Development",
        "Innovation / STI"
    ])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if programme == "Agro-Industrialisation":
        st.markdown("#### Agro-Industrialisation Programme")
        metrics = ["Agri Growth Rate (%)", "Export Value (USD mn)", "Import Value (USD mn)", 
                   "Food Security (%)", "Agri Financing Share (%)", "Annual Jobs (000s)"]
        b = [5.1, 2500, 1096, 71, 11.3, 0]
        t = [8.0, 4800, 600, 85, 15.0, 60]
    elif programme == "Tourism Development":
        st.markdown("#### Tourism Development Programme")
        metrics = ["Forex Earnings (USD bn)", "Length of Stay (nights)", "Spend per Tourist (USD)", 
                   "Satisfaction Score (%)", "Domestic Exp (UGX bn)", "Programme Perf (%)"]
        b = [1.0, 7.6, 1550, 79, 3675, 57.7]
        t = [10.0, 14.0, 3100, 85, 7350, 70.0]
    elif programme == "Extractives Industry":
        st.markdown("#### Extractives Industry Programme")
        metrics = ["Storage Capacity (mn L)", "Oil/Gas Revenue (UGX bn)", "Ugandans Employed (000s)", 
                   "Mineral Value Add Inv (USD bn)", "Oil/Gas Dev Inv (USD bn)", "Programme Perf (%)"]
        b = [99.1, 62.98, 5, 0.8, 0.8, 65]
        t = [150, 265, 50, 2.0, 2.0, 85]
    elif programme == "Private Sector Development":
        st.markdown("#### Private Sector Development")
        metrics = ["Business Lifespan (yrs)", "Informal Sector Size (%)", "Export Value (USD bn)", "Public Contracts to Locals (%)"]
        b = [6, 54.8, 7.9, 64]
        t = [10, 41.5, 10.3, 70]
    else:
        st.markdown("#### Innovation / STI Programme")
        metrics = ["STI Investment (USD mn)", "IDEs Created", "IDEs with Export Market", "STI GDP Contrib (USD bn)", "STI Human Capital (000s)"]
        b = [50, 0, 0, 1, 50]
        t = [500, 50, 10, 10, 500]
        
    df_prog = pd.DataFrame({
        "Indicator": metrics * 2,
        "Value": b + t,
        "Period": ["Baseline"] * len(metrics) + ["Target"] * len(metrics)
    })
    
    fig6 = px.bar(df_prog, x="Indicator", y="Value", color="Period", barmode="group", text="Value",
                  color_discrete_map={"Baseline": COLORS["AMBER"], "Target": COLORS["GREEN"]})
    fig6.update_traces(textposition='outside')
    fig6.update_layout(height=450)
    fig6 = apply_chart_layout(fig6)
    st.plotly_chart(fig6, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 4: Timeline & Projects
# ════════════════════════════════════════════════════════════════════════════
with tab4:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### Lending Rate Reduction Targets")
        lenders = ["Commercial Banks", "Tier 4 Inst", "Money Lenders", "DFIs (e.g. UDB)"]
        lr_base = [18.0, 48.0, 120.0, 12.0]
        lr_tgt = [14.9, 38.0, 60.0, 8.0]
        
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(x=lenders, y=lr_base, name='Current (FY23/24)', marker_color=COLORS['RED']))
        fig7.add_trace(go.Bar(x=lenders, y=lr_tgt, name='Target (FY29/30)', marker_color=COLORS['GREEN']))
        fig7.update_layout(barmode='group', yaxis_title="Interest Rate (%)")
        fig7 = apply_chart_layout(fig7)
        st.plotly_chart(fig7, use_container_width=True)
        
    with col2:
        st.markdown("#### NDPIV High-Impact Projects")
        priority_areas = [
            "Integrated Transport", "Sustainable Energy", "Human Capital", 
            "Knowledge Economy (STI)", "Sustainable Extractives", "Agro-Industrialisation", 
            "Cultural & Sports", "Urban & Housing", "Tourism Dev", 
            "Private Sector Dev", "Monetization of Economy", "Manufacturing"
        ]
        n_projects = [15, 13, 9, 6, 5, 4, 3, 2, 3, 1, 1, 1]
        
        # Sort values
        sorted_pairs = sorted(zip(n_projects, priority_areas))
        n_s, a_s = zip(*sorted_pairs)
        
        fig8 = go.Figure(go.Bar(x=n_s, y=a_s, orientation='h', marker_color=COLORS['TEAL'], text=n_s, textposition='outside'))
        fig8.update_layout(height=450, margin=dict(l=0, r=0, t=10, b=10))
        fig8 = apply_chart_layout(fig8)
        st.plotly_chart(fig8, use_container_width=True)

    st.markdown("---")
    st.markdown("#### NDP Timeline (2010 - 2040)")
    
    # Simplified timeline
    df_timeline = pd.DataFrame([
        dict(Task="NDP I", Start="2010-07-01", Finish="2015-06-30", Status="Completed"),
        dict(Task="NDP II", Start="2015-07-01", Finish="2020-06-30", Status="Completed"),
        dict(Task="NDP III", Start="2020-07-01", Finish="2025-06-30", Status="Running"),
        dict(Task="NDP IV", Start="2025-07-01", Finish="2030-06-30", Status="Running"),
        dict(Task="NDP V", Start="2030-07-01", Finish="2035-06-30", Status="Not Yet"),
        dict(Task="NDP VI", Start="2035-07-01", Finish="2040-06-30", Status="Not Yet")
    ])
    
    color_map = {"Completed": COLORS['GREEN'], "Running": COLORS['AMBER'], "Not Yet": COLORS['GRAY']}
    
    fig9 = px.timeline(df_timeline, x_start="Start", x_end="Finish", y="Task", color="Status", 
                       color_discrete_map=color_map)
    fig9.update_yaxes(autorange="reversed")
    fig9.update_layout(height=300)
    fig9 = apply_chart_layout(fig9)
    st.plotly_chart(fig9, use_container_width=True)

