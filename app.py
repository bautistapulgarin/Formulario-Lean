import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# --- Configuración visual ---
st.set_page_config(page_title="Formulario Auditoría Lean 2026", layout="centered")

# Ocultar menú, header y footer
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
try:
    # Cargar JSON desde Streamlit Secrets
    secrets_json = st.secrets["google_service_account"]["json"]
    credentials_dict = json.loads(secrets_json)

    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
    gc = gspread.authorize(credentials)

    # Abrir la hoja usando el nombre exacto
    sheet = gc.open("Formulario auditoria lean 2026").sheet1
except Exception as e:
    st.error(f"Error al conectar con Google Sheets: {e}")
    st.stop()

# --- Campos de formulario ---
nombre = st.text_input("Nombre del inspector")
observacion = st.text_area("Observaciones")

# --- Botón de registro ---
if st.button("Registrar en Google Sheets"):
    if nombre.strip() == "":
        st.warning("Debe ingresar un nombre.")
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([now, nombre, observacion])
        st.success("¡Registro agregado correctamente en Google Sheets!")
