import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Leer credenciales desde Secrets
creds_dict = json.loads(st.secrets["GSPREAD_CREDS"])

# Configurar acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Abrir hoja por ID
sheet = client.open_by_key("1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4").sheet1

# Leer datos
st.write(sheet.get_all_records())
