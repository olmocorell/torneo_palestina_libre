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
  {'nombre': 'Ana', 'pronombre': 'ella'}],
 'MiniTransket': [{'nombre': 'Lucas', 'pronombre': 'él'},
  {'nombre': 'Julls', 'pronombre': 'elle'},
  {'nombre': 'Lau', 'pronombre': 'él/elle'},
  {'nombre': 'Olmo', 'pronombre': 'él/elle'}],
 'Entxantxe ': [{'nombre': 'Irene', 'pronombre': 'ella'},
  {'nombre': 'Lucia', 'pronombre': 'ella'},
  {'nombre': 'Sabela', 'pronombre': 'ella'},
  {'nombre': 'Luque', 'pronombre': 'ella'}],
 'Keffiyeh': [{'nombre': 'Irene/Saltamontes', 'pronombre': 'elle'},
  {'nombre': 'Alba J.', 'pronombre': 'ella'},
  {'nombre': 'Alicia', 'pronombre': 'ella'}],
 'Unikuirnios': [{'nombre': 'Tere', 'pronombre': 'ella'},
  {'nombre': 'Belén', 'pronombre': 'ella'},
  {'nombre': 'Lau', 'pronombre': 'él/elle'}],
 'Marsha.P': [{'nombre': 'Silvia', 'pronombre': 'ella'},
  {'nombre': 'Rakel', 'pronombre': 'ella'},
  {'nombre': 'Astro', 'pronombre': 'ella'}],
 'Stonewalls': [{'nombre': 'Tania', 'pronombre': 'ella/elle'},
  {'nombre': 'Inês', 'pronombre': 'ella'},
  {'nombre': 'Alicia', 'pronombre': 'ella'},
  {'nombre': 'Paula', 'pronombre': 'ella'}],
 'GenderFluid': [{'nombre': 'Herminia Páez Prado', 'pronombre': 'ella/elle'},
  {'nombre': 'Arin', 'pronombre': 'ella'},
  {'nombre': 'Paula Carrión', 'pronombre': 'ella'},
  {'nombre': 'Marc', 'pronombre': 'él'}],
 'Falafel': [{'nombre': 'Colaso', 'pronombre': 'ella/elle'},
  {'nombre': 'Laura', 'pronombre': 'ella'},
  {'nombre': 'Toni', 'pronombre': 'él/ella/elle'}],
 'Olivos': [{'nombre': 'Patri', 'pronombre': 'elle/ella'},
  {'nombre': 'Azul', 'pronombre': 'Ella/Elle'},
  {'nombre': 'Bea', 'pronombre': 'ella'}],
 'Ahed Tamimi': [{'nombre': 'Alba Esparza', 'pronombre': 'ella'},
  {'nombre': 'Gaia', 'pronombre': 'elle/ella'},
  {'nombre': 'Olga', 'pronombre': 'ella'},
  {'nombre': 'Dany', 'pronombre': 'él'}],
 'Marais': [{'nombre': 'Noemí', 'pronombre': 'ella'},
  {'nombre': 'Olaya', 'pronombre': 'elle/ella'},
  {'nombre': 'Sara', 'pronombre': 'ella'}]}

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
