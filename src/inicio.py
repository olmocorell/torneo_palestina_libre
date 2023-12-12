import streamlit as st

def inicio():
    st.image('assets/cabecera.png', use_column_width=True)
    st.markdown("""#### Bienvenide al torneo :flag-ps: Palestina Libre :flag-ps: organizado por la Liga Gamberra""")
    st.markdown(":rocket: :fire: Estamos encantades de que hayas venido :rocket: :fire:")
    st.markdown("""
                Antes de empezar, recuerda que jugamos bajo algunos acuerdos:        
                - :heart: Usamos el pronombre neutro (elle). También puedes preguntar los pronombres.    
                - :heart: Pitamos las propias faltas y las del otro equipo, si es necesario.       
                - :heart: Existe una figura de 'cuidadore' por equipo para mediar si hace falta y trasladar malestares.       
                - :heart: Jugamos para disfrutar, no para derrotar al otro equipo por 'paliza'.        
                - :heart: Priorizamos el buen rollo y las ganas de pasarlo bien.      

                Estás en un espacio transfeminista y libre de violencias, échanos una mano para mantener el espacio seguro.
                """, unsafe_allow_html=True)
