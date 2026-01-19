import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# Configuración Streamlit
st.set_page_config(page_title="Formulario base", layout="centered")

# CSS para ocultar menú y footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Formulario en construcción")
st.write("Prueba de conexión con Google Sheets")

# --- Conexión con Google Sheets ---
secrets_json = st.secrets["google_service_account"]["json"]
credentials_dict = json.loads(secrets_json)

scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
gc = gspread.authorize(credentials)

# Abre la hoja (por nombre)
sheet = gc.open("registro_formulario_streamlit").sheet1

# --- Botón de prueba ---
if st.button("Registrar prueba"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, "Nombre de prueba", "Observación de prueba"])
    st.success("¡Registro agregado en Google Sheets!")
