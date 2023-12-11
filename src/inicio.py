import streamlit as st

def inicio():
    st.title("Bienvenide al torneo")
    st.image('assets/cabecera.png', use_column_width=True)
    st.markdown("""
                Recuerda que seguimos algunas normas:
                - :heart: Usamos el pronombre neutro (elle) si no sabemos los pronombres.
                - :heart: Pitamos las propias faltas y las del otro equipo, si es necesario.
                - :heart: Existe una figura de 'cuidadore' por equipo para mediar si hace falta y trasladar malestares.
                - :heart: Jugamos para disfrutar, no para derrotar al otro equipo por 'paliza'.
                - :heart: Priorizamos el buen rollo y las ganas de pasarlo bien.

                Estás en un espacio transfeminista y libre de violencias para mantener el espacio seguro.
                """, unsafe_allow_html=True)
