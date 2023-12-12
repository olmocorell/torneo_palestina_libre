import streamlit as st
import time
from datetime import datetime, timedelta
from collections import defaultdict
from src.utiles import horarios

def obtener_partidos_en_curso_y_siguientes(hora_actual, horarios, duracion_partido=10):
    en_curso = defaultdict(list)
    siguientes = defaultdict(list)
    tiempos_futuros = sorted({datetime.strptime(tiempo, '%H:%M').time() for tiempo, _ in horarios if
                              datetime.strptime(tiempo, '%H:%M').time() > hora_actual})

    # Obtener los dos próximos bloques de tiempo
    proximos_bloques = tiempos_futuros[:2]

    for tiempo, partido in horarios:
        hora_partido = datetime.strptime(tiempo, '%H:%M').time()
        fin_partido = (datetime.combine(datetime.today(), hora_partido) + timedelta(minutes=duracion_partido)).time()

        if hora_partido <= hora_actual < fin_partido:
            en_curso[tiempo].append(partido)
        elif hora_partido in proximos_bloques:
            siguientes[tiempo].append(partido)

    return en_curso, siguientes

def asignar_pistas(horarios):
    resultado = defaultdict(dict)
    for tiempo, juegos in horarios.items():
        for i, juego in enumerate(juegos):
            pista = i % 4 + 1  # Asigna pistas 1-4 en ciclo
            resultado[tiempo][f"Pista {pista}"] = juego
    return resultado

def mostrar_partidos():
    st.markdown("## 🏀 Programación de los Partidos 🏀")
    st.markdown("""
    #### ⏰ ¡No te pierdas ningún partido!
    **Permanece atento/a a esta página para seguir los horarios en tiempo real.** A continuación, se muestran los partidos que están en curso y los próximos a jugarse.
    Esta información se actualiza según los horarios planificados. 
    """)

    # Actualización automática cada minuto
    while True:
        # Obtiene la hora actual
        hora_actual = datetime.now().time()

        en_curso, siguientes = obtener_partidos_en_curso_y_siguientes(hora_actual, horarios)
        en_curso_con_pistas = asignar_pistas(en_curso)
        siguientes_con_pistas = asignar_pistas(siguientes)

        st.markdown("### 🏆 Partidos en Curso")
        for tiempo, partidos in en_curso_con_pistas.items():
            st.markdown(f"**{tiempo}**")
            for pista, equipos in partidos.items():
                st.markdown(f"- {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

        st.markdown("### 🕒 Próximos Partidos")
        for tiempo, partidos in siguientes_con_pistas.items():
            st.markdown(f"**{tiempo}**")
            for pista, equipos in partidos.items():
                st.markdown(f"- {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

        # Espera 60 segundos antes de actualizar
        time.sleep(120)
        st.experimental_rerun()

# Llama a la función en tu app Streamlit
mostrar_partidos()