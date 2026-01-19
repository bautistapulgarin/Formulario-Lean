import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime

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
try:
    secrets_json = st.secrets["google_service_account"]["json"]
    credentials_dict = json.loads(secrets_json)
    
    # Reemplazar saltos de línea reales en private_key
    credentials_dict["private_key"] = credentials_dict["private_key"].replace("\\n", "\n")

    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
    gc = gspread.authorize(credentials)

    sheet = gc.open("Formulario auditoria lean 2026").sheet1
except Exception as e:
    st.error(f"Error al conectar con Google Sheets: {e}")
    st.stop()

# --- Formulario ---
nombre = st.text_input("Nombre del inspector")
observacion = st.text_area("Observaciones")

if st.button("Registrar en Google Sheets"):
    if nombre.strip() == "":
        st.warning("Debe ingresar un nombre.")
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([now, nombre, observacion])
        st.success("¡Registro agregado correctamente en Google Sheets!")
