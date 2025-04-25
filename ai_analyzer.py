import openai
import streamlit as st

openai.api_key = st.secrets["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"]

def analyze_airbnb_data(data):
    prompt = f"Analyze this Airbnb data for most profitable units:
{data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
