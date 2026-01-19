import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

# Leer credenciales desde secrets
creds_dict = json.loads(st.secrets["GSPREAD_CREDS"])

# Definir alcance de Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

# Crear credenciales
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# Conectar con Google Sheets
client = gspread.authorize(creds)

# Abrir hoja por ID
sheet = client.open_by_key("1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4").sheet1

# Leer datos
st.write(sheet.get_all_records())
