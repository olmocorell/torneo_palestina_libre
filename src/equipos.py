import streamlit as st

def buscar_equipo(nombre, equipos):
    nombre = nombre.lower()
    for equipo, miembros in equipos.items():
        for miembro in miembros:
            if nombre == miembro['nombre'].lower():
                return equipo
    return None

def mostrar_equipos(equipos):
    for nombre_equipo, miembros in equipos.items():
        st.markdown(f"### {nombre_equipo}")
        for miembro in miembros:
            st.markdown(f"- {miembro['nombre']} ({miembro['pronombre']})")
        st.markdown("---")

def equipos():
    # Diccionario de ejemplo con pronombres, reemplázalo con tus datos
    equipos_dict = {'Lagartos furtivos': [{'nombre': 'Paula', 'pronombre': 'ella'},
                           {'nombre': 'Arantxa', 'pronombre': 'ella'},
                           {'nombre': 'Llun', 'pronombre': 'él'}],
     'Les girasoles': [{'nombre': 'Nats', 'pronombre': 'elle'},
                       {'nombre': 'Kai', 'pronombre': 'ella/él/elle'},
                       {'nombre': 'Vero', 'pronombre': 'ella'}],
     'Conde Duquesa Basket Club': [{'nombre': 'Almudena', 'pronombre': 'ella'},
                                   {'nombre': 'Rocío', 'pronombre': 'ella'},
                                   {'nombre': 'Sonia', 'pronombre': 'ella'}],
     'Mantis ': [{'nombre': 'Nuria', 'pronombre': 'ella'},
                 {'nombre': 'MP', 'pronombre': 'ella/elle'},
                 {'nombre': 'Carol', 'pronombre': 'ella'},
                 {'nombre': 'Laura', 'pronombre': 'ella'},
                 {'nombre': 'Ana', 'pronombre': 'ella'}]}

    st.markdown("""
       #### 🌟🌈 Distribución de Equipos 🌈🌟
       ---
       """)

    # Campo para buscar el equipo de una persona
    nombre_busqueda = st.text_input("Introduce tu nombre para saber en qué equipo estás:")
    if nombre_busqueda:
        equipo_encontrado = buscar_equipo(nombre_busqueda, equipos_dict)
        if equipo_encontrado:
            st.write(f"Creo que tu equipo es **{equipo_encontrado}**. Pero revisa la página, si tienes dudas habla con la organización.")
        else:
            st.write("No se ha encontrado tu equipo. Por favor, revisa la página o habla con la organización.")



    # Mostrar equipos usando el diccionario
    mostrar_equipos(equipos_dict)

# Llama a la función en tu app Streamlit
equipos()
