import streamlit as st

# Configuración básica
st.set_page_config(
    page_title="Formulario base",
    layout="centered"
)

# CSS para ocultar elementos de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Contenido principal
st.title("Formulario en construcción")
st.write("Este es el punto de partida del formulario.")
