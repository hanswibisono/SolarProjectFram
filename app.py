# ============================================================
# SOLAR PROJECT FINANCIAL CALCULATOR
# ============================================================

import streamlit as st        # the dashboard framework
import pandas as pd            # for creating and displaying tables
import numpy_financial as npf  # for IRR calculation (npf.irr)

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Solar Project Calculator",
    layout="wide"
)

# TITLE & DESCRIPTION
st.title("Solar Project Financial Calculator")
st.caption("25-year cash flow model · All-equity · No financing costs")

# MODEL ASSUMPTIONS (CONSTANTS)
COST_PER_W  = 2.50    # $2.50 per watt installed cost
GEN_PER_KW  = 1400    # 1,400 kWh generated per kW per year
ESCALATION  = 0.025   # electricity price grows 2.5% per year
OM_PER_KW   = 15      # $15 per kW per year for operations & maintenance
ITC         = 0.30    # 30% Investment Tax Credit applied in Year 0
YEARS       = 25      # project lifetime

# ELECTRICITY RATES BY STATE
# State residential electricity rate in ¢/kWh
# Source: ElectricChoice.com, May 2026

STATE_RATES = {
    "Alabama": 16.79, "Alaska": 26.57, "Arizona": 15.62,
    "Arkansas": 13.32, "California": 33.75, "Colorado": 16.33,
    "Connecticut": 27.84, "Delaware": 18.39, "District of Columbia": 24.03,
    "Florida": 15.77, "Georgia": 14.60, "Hawaii": 39.89,
    "Idaho": 12.51, "Illinois": 18.82, "Indiana": 17.42,
    "Iowa": 13.54, "Kansas": 15.23, "Kentucky": 13.68,
    "Louisiana": 12.44, "Maine": 29.55, "Maryland": 22.40,
    "Massachusetts": 31.51, "Michigan": 20.55, "Minnesota": 16.44,
    "Mississippi": 14.53, "Missouri": 13.01, "Montana": 14.33,
    "Nebraska": 13.19, "Nevada": 13.83, "New Hampshire": 25.12,
    "New Jersey": 22.48, "New Mexico": 15.09, "New York": 23.44,
    "North Carolina": 14.37, "North Dakota": 12.71, "Ohio": 16.81,
    "Oklahoma": 13.44, "Oregon": 14.22, "Pennsylvania": 18.15,
    "Rhode Island": 28.43, "South Carolina": 15.22, "South Dakota": 14.11,
    "Tennessee": 13.77, "Texas": 15.10, "Utah": 12.89,
    "Vermont": 22.76, "Virginia": 15.92, "Washington": 12.93,
    "West Virginia": 13.11, "Wisconsin": 18.06, "Wyoming": 12.55
}

# KEY INPUTS
st.subheader("Inputs")
col1, col2 = st.columns(2)

# Dropdown to select a US state
with col1 :
    selected_state = st.selectbox(
    label="US State",
    options=sorted(STATE_RATES.keys()),
    index=sorted(STATE_RATES.keys()).index("New York")
)

# Number input for system size
with col2 :
    system_size_kw = st.number_input(
    label="System size (kW DC)",
    min_value=1,
    max_value=1000,
    value=10,
    step=1,
    key="system_size"
)

# SIDEBAR
st.sidebar.subheader("Model assumptions")
st.sidebar.caption(f"Installed cost: ${COST_PER_W}/W")
st.sidebar.caption(f"Generation: {GEN_PER_KW:,} kWh/kW/yr")
st.sidebar.caption(f"Electricity escalation: {ESCALATION*100:.1f}%/yr")
st.sidebar.caption(f"O&M cost: ${OM_PER_KW}/kW/yr")
st.sidebar.caption(f"ITC: {int(ITC*100)}% in Year 0")
st.sidebar.caption("Source: ElectricChoice.com (May 2026)")
