import streamlit as st
from datetime import datetime, timezone
import pytz

# Suponiendo que este es el módulo que contiene tus horarios de partidos
from src.utiles import horarios

def obtener_partidos_en_curso_y_siguientes(hora_actual, horarios, max_siguientes=5):
    en_curso = []
    siguientes_temp = []

    for inicio, fin, pista, equipos in horarios:
        hora_inicio = datetime.strptime(inicio, '%H:%M').time()
        hora_fin = datetime.strptime(fin, '%H:%M').time()

        if hora_inicio <= hora_actual < hora_fin:
            en_curso.append((inicio, pista, equipos))
        elif hora_actual < hora_inicio:
            siguientes_temp.append((inicio, pista, equipos))

    # Ordenar los partidos siguientes por hora de inicio y limitar la cantidad
    siguientes_temp.sort(key=lambda x: datetime.strptime(x[0], '%H:%M').time())
    siguientes = siguientes_temp[:max_siguientes]

    return en_curso, siguientes

def mostrar_partidos():

    hora_actual_utc = datetime.now(timezone.utc)
    zona_horaria_madrid = pytz.timezone("Europe/Madrid")
    hora_actual_madrid = hora_actual_utc.astimezone(zona_horaria_madrid).time()

    en_curso, siguientes = obtener_partidos_en_curso_y_siguientes(hora_actual_madrid, horarios)

    st.markdown(""" #### ⏰👀 ¡No te pierdas ningún partido!👀⏰
    ---
    **Permanece atente a esta página para seguir los horarios en tiempo real.** 
    A continuación, se muestran los partidos que están en curso y los próximos a jugarse.     
    Esta información se actualiza según los horarios planificados, no según lo que está sucediendo, depende de que estemos siendo puntuales.      
    Si ves desfase con la hora que es, pulsa el botón para que refresque :point_down:
    """)

    if st.button('Actualizar Partidos :arrows_counterclockwise:'):
        st.experimental_rerun()

    st.markdown("### 🏆 Partidos en Curso")
    for tiempo, pista, equipos in en_curso:
        st.markdown(f"- Han empezado a las **{tiempo}** en Pista {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

    st.markdown("### 🕒 Próximos Partidos")
    for tiempo, pista, equipos in siguientes:
        st.markdown(f"- Empiezan a las **{tiempo}** en Pista {pista}: *Equipo {equipos[0]}* vs *Equipo {equipos[1]}*")

mostrar_partidos()
