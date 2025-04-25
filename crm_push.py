import requests
import streamlit as st

HUBSPOT_API_KEY = st.secrets["HUBSPOT_API_KEY"]

def push_to_crm(data):
    url = "https://api.hubapi.com/crm/v3/objects/custom_objects"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }
    requests.post(url, json={"properties": data}, headers=headers)
