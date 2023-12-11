import streamlit as st
from datetime import datetime, timedelta
from collections import defaultdict

def obtener_partidos_en_curso_y_siguientes(hora_actual, partidos, duracion_partido=10):
    en_curso = defaultdict(list)
    siguientes = defaultdict(list)
    tiempos_futuros = sorted({datetime.strptime(tiempo, '%H:%M').time() for tiempo, _ in partidos if
                              datetime.strptime(tiempo, '%H:%M').time() > hora_actual})

    # Obtener los dos próximos bloques de tiempo
    proximos_bloques = tiempos_futuros[:2]

    for tiempo, partido in partidos:
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
            pista = i % 4 + 1  # Asigna pistas 1-4 en ciclo
            resultado[tiempo][f"Pista {pista}"] = juego
    return resultado


def main():
    partidos = [('16:50', (4, 16)),
 ('16:50', (3, 15)),
 ('16:50', (12, 14)),
 ('16:50', (9, 10)),
 ('17:01', (7, 13)),
 ('17:01', (1, 6)),
 ('17:01', (5, 11)),
 ('17:01', (2, 8)),
 ('17:12', (4, 14)),
 ('17:12', (7, 16)),
 ('17:12', (3, 9)),
 ('17:12', (2, 12)),
 ('17:23', (6, 8)),
 ('17:23', (1, 5)),
 ('17:23', (10, 15)),
 ('17:23', (11, 13)),
 ('17:34', (2, 4)),
 ('17:34', (7, 14)),
 ('17:34', (12, 16)),
 ('17:34', (1, 15)),
 ('17:45', (3, 10)),
 ('17:45', (6, 11)),
 ('17:45', (5, 13)),
 ('17:45', (8, 9)),
 ('17:56', (3, 4)),
 ('17:56', (14, 16)),
 ('17:56', (1, 7)),
 ('17:56', (9, 12)),
 ('18:07', (6, 13)),
 ('18:07', (5, 15)),
 ('18:07', (8, 11)),
 ('18:07', (2, 10)),
 ('18:18', (4, 9)),
 ('18:18', (14, 15)),
 ('18:18', (3, 12)),
 ('18:18', (1, 16))]
    st.title("Programación de Partidos")

    # Obtiene la hora actual
    hora_actual = datetime.now().time()

    en_curso, siguientes = obtener_partidos_en_curso_y_siguientes(hora_actual, partidos)
    en_curso_con_pistas = asignar_pistas(en_curso)
    siguientes_con_pistas = asignar_pistas(siguientes)

    st.subheader("Partidos en Curso")
    for tiempo, partidos in en_curso_con_pistas.items():
        st.markdown(f"### {tiempo}")
        for pista, equipos in partidos.items():
            st.write(f"{pista}: Equipo {equipos[0]} vs Equipo {equipos[1]}")

    st.subheader("Próximos Partidos")
    for tiempo, partidos in siguientes_con_pistas.items():
        st.markdown(f"### {tiempo}")
        for pista, equipos in partidos.items():
            st.write(f"{pista}: Equipo {equipos[0]} vs Equipo {equipos[1]}")


if __name__ == "__main__":
    main()
