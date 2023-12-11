import streamlit as st
from streamlit_option_menu import option_menu
from src.partidos import partidos
from src.equipos import equipos

st.set_page_config(page_title="Torneo Palestina Libre", page_icon=":basketball:", layout="wide", menu_items={
    'Get Help': None,
    'Report a bug': None,
    'About': None
})

# Crea un menú de opciones en la barra lateral
with st.sidebar:
    selected = option_menu("Menú del torneo", ["Inicio", "Síguelo en directo"],
                           icons=['house', 'camera'], menu_icon="fa-basketball", default_index=0)

# Diccionario para mapear nombres a funciones
page_names_to_funcs = {
    "Inicio": equipos,
    "Síguelo en directo": partidos,
}

# Ejecución de la función seleccionada
if selected in page_names_to_funcs:
    page_names_to_funcs[selected]()