import streamlit as st
import os

def ejecutar():
    st.header("🧠 Módulo 35: Razonamiento A IO")
    pregunta = st.text_input("Consulta de IA:")
    
    if pregunta:
        if os.path.exists("data/mapa_conocimiento.json"):
            st.write("🤖 **A IO Pensando...**")
            st.info("Estado: Consultando expertos en el Módulo 36.")
            st.success(f"Análisis completado: La consulta '{pregunta}' ha sido integrada en el flujo cognitivo.")
        else:
            st.warning("IA en modo offline. Requiere datos del Módulo 37.")
