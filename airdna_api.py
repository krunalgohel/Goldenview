import requests
import streamlit as st

AIRDNA_API_KEY = st.secrets["AIRDNA_API_KEY"]

def get_airbnb_data():
    headers = {"Authorization": f"Bearer {AIRDNA_API_KEY}"}
    response = requests.get("https://api.airdna.co/v1/sample-data", headers=headers)
    return response.json()
