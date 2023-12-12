import streamlit as st
from datetime import datetime, timedelta, timezone
from collections import defaultdict
import pytz

from src.utiles import horarios

@st.cache_data
def obtener_partidos_en_curso_y_siguientes(hora_actual, horarios, duracion_partido=10):
    en_curso = defaultdict(list)
    siguientes = defaultdict(list)
    tiempos_futuros = sorted({datetime.strptime(tiempo, '%H:%M').time() for tiempo, _ in horarios if
                              datetime.strptime(tiempo, '%H:%M').time() > hora_actual})

    proximos_bloques = tiempos_futuros[:2]

    for tiempo, partido in horarios:
        hora_partido = datetime.strptime(tiempo, '%H:%M').time()
        fin_partido = (datetime.combine(datetime.today(), hora_partido) + timedelta(minutes=duracion_partido)).time()

        if hora_partido <= hora_actual < fin_partido:
            en_curso[tiempo].append(partido)
        elif hora_partido in proximos_bloques:
            siguientes[tiempo].append(partido)

    return en_curso, siguientes

def asignar_pistas(partidos):
    resultado = defaultdict(dict)
    for tiempo, juegos in partidos.items():
        for i, juego in enumerate(juegos):
            pista = i % 4 + 1
            resultado[tiempo][f"Pista {pista}"] = juego
    return resultado

def mostrar_partidos():
    st.markdown("## 🏀 Programación de los Partidos 🏀")

    hora_actual_utc = datetime.now(timezone.utc)
    zona_horaria_madrid = pytz.timezone("Europe/Madrid")
    hora_actual_madrid = hora_actual_utc.astimezone(zona_horaria_madrid).time()

    en_curso, siguientes = obtener_partidos_en_curso_y_siguientes(hora_actual_madrid, horarios)
    en_curso_con_pistas = asignar_pistas(en_curso)
    siguientes_con_pistas = asignar_pistas(siguientes)

    st.markdown("""
    #### ⏰ ¡No te pierdas ningún partido!
    **Permanece atente a esta página para seguir los horarios en tiempo real.** 
    A continuación, se muestran los partidos que están en curso y los próximos a jugarse.
    Esta información se actualiza según los horarios planificados, no según lo que está sucediendo, depende de que estemos siendo puntuales. 
    Si ves desfase con la hora que es, pulsa el botón para que refresque :point_down:
    """)

    if st.button('Actualizar Partidos :arrows_counterclockwise:'):
        st.experimental_rerun()

    st.markdown("### 🏆 Partidos en Curso")
    for tiempo, partidos in en_curso_con_pistas.items():
        st.markdown(f"Han empezado a las **{tiempo}**")
        for pista, equipos in partidos.items():
            st.markdown(f"- {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

    st.markdown("### 🕒 Próximos Partidos")
    for tiempo, partidos in siguientes_con_pistas.items():
        st.markdown(f"Empiezan a las **{tiempo}**")
        for pista, equipos in partidos.items():
            st.markdown(f"- {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

mostrar_partidos()
