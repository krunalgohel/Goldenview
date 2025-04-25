import streamlit as st
from ai_analyzer import analyze_airbnb_data

st.title("Airbnb Profitability Analyzer 💰")

uploaded_file = st.file_uploader("Upload your Airbnb data (CSV)", type="csv")

if uploaded_file is not None:
    data = uploaded_file.read().decode("utf-8")
    st.subheader("Raw Data")
    st.text(data)

    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            result = analyze_airbnb_data(data)
            st.subheader("AI Analysis")
            st.write(result)
