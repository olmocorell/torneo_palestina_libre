import streamlit as st
import pandas as pd
from src.utiles import horarios

# Verificación de la importación de los horarios
st.write("Datos importados:", horarios)

# Convertir la lista de horarios a un DataFrame
df_horarios = pd.DataFrame(horarios, columns=['Hora de Inicio', 'Hora de Fin', 'Pista', 'Equipos'])

# Verificación del DataFrame
st.write("DataFrame de los horarios:", df_horarios)

# Formatear la columna 'Equipos' para mostrar los nombres separados
df_horarios['Equipos'] = df_horarios['Equipos'].apply(lambda x: f"{x[0]} vs {x[1]}")

def horario():
    # Encabezado de la página
    st.markdown(""" #### ⏰🏀 Horario de Partidos 🏀⏰
    ---
    Aquí tienes todo el calendario de la jornada para que sepas a qué hora te toca jugar.        
    ¡Sé puntual!        
    Estate preparade con tu equipo cerca de la pista cuando se acerque la hora de jugar      
    ¡Gracias!
    """)

    # Mostrar la tabla de horarios
    st.markdown("## Horarios de los Partidos")
    st.table(df_horarios)

horario()
