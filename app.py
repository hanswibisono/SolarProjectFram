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
