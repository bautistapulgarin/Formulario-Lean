import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Ruta del JSON en el repo
json_file = "credentials.json"

# Alcances
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

# Credenciales
creds = Credentials.from_service_account_file(json_file, scopes=scope)
client = gspread.authorize(creds)

# Abrir hoja
sheet = client.open_by_key("1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4").sheet1
st.write(sheet.get_all_records())
