import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import json

# Cargar el JSON del secreto
secrets_json = st.secrets["google_service_account"]["json"]
credentials_dict = json.loads(secrets_json)

scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
gc = gspread.authorize(credentials)

sheet = gc.open("registro_formulario_streamlit").sheet1

if st.button("Registrar prueba"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, "Nombre de prueba", "Observación de prueba"])
    st.success("¡Registro agregado en Google Sheets!")
