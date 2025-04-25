import streamlit as st
from ai_analyzer import analyze_airbnb_data
from airdna_api import get_airbnb_data
from crm_push import push_to_crm
from google_sheets_exporter import export_to_google_sheets

st.set_page_config(page_title="GoldenView", layout="wide")
st.title("GoldenView: Airbnb Profitability Analyzer")
st.markdown("Discover the most profitable Airbnb units across the U.S. — powered by AI + real-time market data.")

if st.button("Fetch & Analyze Data"):
    raw_data = get_airbnb_data()
    insights = analyze_airbnb_data(raw_data)
    st.json(insights)
    export_to_google_sheets(insights)
    push_to_crm(insights)
    st.success("Data pushed to Google Sheets and CRM!")
