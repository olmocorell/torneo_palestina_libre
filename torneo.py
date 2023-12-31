import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Torneo Palestina Libre", page_icon=":basketball:", layout="wide", menu_items={
    'Get Help': None,
    'Report a bug': None,
    'About': None
})
from src.partidos import mostrar_partidos
from src.equipos import equipos
from src.inicio import inicio
from src.horarios import horario

# Crea un menú de opciones en la barra lateral
with st.sidebar:
    selected = option_menu("Menú del torneo", ["Inicio", "Horario", "Equipos","Síguelo en directo"],
                           icons=['house', 'clock', 'people', 'camera'], menu_icon="fa-basketball", default_index=0)

# Diccionario para mapear nombres a funciones
page_names_to_funcs = {
    "Inicio": inicio,
    "Síguelo en directo": mostrar_partidos,
    "Equipos": equipos,
    "Horario": horario
}

# Ejecución de la función seleccionada
if selected in page_names_to_funcs:
    page_names_to_funcs[selected]()
