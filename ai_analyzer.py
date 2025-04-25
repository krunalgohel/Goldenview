import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def analyze_airbnb_data(data):
    prompt = f"Analyze this Airbnb data for most profitable units:
{data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
