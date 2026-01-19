import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# --- Configuración visual ---
st.set_page_config(page_title="Formulario Auditoría Lean 2026", layout="centered")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Formulario Auditoría Lean 2026")
st.write("Registro de prueba en Google Sheets")

# --- Conexión con Google Sheets ---
# Cargar JSON desde Streamlit Secrets
secrets_json = st.secrets["google_service_account"]["json"]
credentials_dict = json.loads(secrets_json)

scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
gc = gspread.authorize(credentials)

# Abrir la hoja usando el nombre exacto
sheet = gc.open("Formulario auditoria lean 2026").sheet1

# --- Botón de prueba ---
if st.button("Registrar prueba"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Puedes agregar más campos según tu formulario
    sheet.append_row([now, "Nombre de prueba", "Observación de prueba"])
    st.success("¡Registro agregado en Google Sheets!")
