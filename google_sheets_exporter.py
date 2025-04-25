import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def export_to_google_sheets(data, sheet_name="GoldenViewData"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["google"], scope)
    client = gspread.authorize(creds)
    sheet = client.create(sheet_name).sheet1
    for i, (k, v) in enumerate(data.items(), start=1):
        sheet.update_cell(i, 1, k)
        sheet.update_cell(i, 2, v)
