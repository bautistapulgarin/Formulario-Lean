import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------
# CONFIGURACIÓN GOOGLE SHEETS
# -------------------------------
JSON_FILE = "leanauditoria-9315e4255edb.json"  # JSON subido en Streamlit Cloud
SHEET_ID = "1G8GvBqkTs7WamLRe_h-s9tJxRCCsNtmZEl15WXIggP4"  # ID de la hoja

# Alcances necesarios
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Conexión y autenticación
try:
    creds = Credentials.from_service_account_file(JSON_FILE, scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
except Exception as e:
    st.error("No se pudo conectar con Google Sheets. "
             "Verifica que la hoja esté compartida con el service account y que el JSON sea correcto.")
    st.stop()

# -------------------------------
# CONFIGURACIÓN STREAMLIT
# -------------------------------
st.set_page_config(page_title="Formulario Lean Auditoria", layout="centered")
st.title("Formulario Lean Auditoria")
st.write("Completa los campos para registrar información del proyecto.")

# Ocultar menú, header y footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------------------
# FORMULARIO DE DATOS
# -------------------------------
with st.form(key="lean_form"):
    nombre = st.text_input("Nombre del responsable")
    proyecto = st.text_input("Nombre del proyecto")
    avance = st.number_input("Avance (%)", min_value=0, max_value=100)
    observaciones = st.text_area("Observaciones")

    submit_button = st.form_submit_button("Enviar")

# -------------------------------
# GUARDAR DATOS EN GOOGLE SHEETS
# -------------------------------
if submit_button:
    if not nombre.strip() or not proyecto.strip():
        st.warning("Por favor completa los campos Nombre y Proyecto antes de enviar.")
    else:
        try:
            nueva_fila = [nombre, proyecto, avance, observaciones]
            sheet.append_row(nueva_fila)
            st.success("Datos enviados correctamente!")
        except Exception as e:
            st.error("Ocurrió un error al enviar los datos. "
                     "Verifica los permisos de la hoja y vuelve a intentarlo.")
