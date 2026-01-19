import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------
# Configuración de la hoja de Google
# -------------------------------
JSON_FILE = "leanauditoria-9315e4255edb.json"  # tu JSON subido
SHEET_ID = "1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4"  # ID de la hoja

# Alcances de Google Sheets
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

# Autenticación
creds = Credentials.from_service_account_file(JSON_FILE, scopes=scope)
client = gspread.authorize(creds)

# Abrir hoja
sheet = client.open_by_key(SHEET_ID).sheet1

# -------------------------------
# Streamlit: Formulario
# -------------------------------
st.set_page_config(page_title="Formulario Lean Auditoria", layout="centered")
st.title("Formulario Lean Auditoria")

with st.form(key="lean_form"):
    nombre = st.text_input("Nombre del responsable")
    proyecto = st.text_input("Nombre del proyecto")
    avance = st.number_input("Avance (%)", min_value=0, max_val_
