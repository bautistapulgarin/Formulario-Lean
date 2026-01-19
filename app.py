import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------
# Configuración de Google Sheets
# -------------------------------
JSON_FILE = "leanauditoria-9315e4255edb.json"  # Tu archivo JSON subido
SHEET_ID = "1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4"  # ID de la hoja

# Alcances de Google Sheets y Drive
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Autenticación
creds = Credentials.from_service_account_file(JSON_FILE, scopes=scope)
client = gspread.authorize(creds)

# Abrir la primera hoja
sheet = client.open_by_key(SHEET_ID).sheet1

# -------------------------------
# Configuración de Streamlit
# -------------------------------
st.set_page_config(page_title="Formulario Lean Auditoria", layout="centered")
st.title("Formulario Lean Auditoria")
st.write("Por favor completa los campos para registrar la información del proyecto.")

# CSS para ocultar menú y footer de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------------------
# Formulario de datos
# -------------------------------
with st.form(key="lean_form"):
    nombre = st.text_input("Nombre del responsable")
    proyecto = st.text_input("Nombre del proyecto")
    avance = st.number_input("Avance (%)", min_value=0, max_value=100)
    observaciones = st.text_area("Observaciones")

    submit_button = st.form_submit_button("Enviar")

# -------------------------------
# Guardar datos en Google Sheets
# -------------------------------
if submit_button:
    if nombre.strip() == "" or proyecto.strip() == "":
        st.warning("Por favor completa los campos Nombre y Proyecto antes de enviar.")
    else:
        nueva_fila = [nombre, proyecto, avance, observaciones]
        sheet.append_row(nueva_fila)
        st.success("Datos enviados correctamente!")
