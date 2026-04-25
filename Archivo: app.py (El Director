import streamlit as st
import os

st.set_page_config(page_title="A IO - Cerebro", layout="wide")

st.sidebar.title("🧠 A IO: Intelligence")
opcion = st.sidebar.radio("Seleccionar Módulo:", 
    ["Inicio", "35: Razonamiento", "36: Buscador", "37: Ingesta"])

if opcion == "Inicio":
    st.title("🌐 A IO - Cerebro de Datos")
    st.write("Bienvenido al núcleo de procesamiento masivo.")
    if os.path.exists("data/mapa_conocimiento.json"):
        st.success("Estado: Conocimiento Cargado.")
    else:
        st.warning("Estado: Memoria Vacía. Usa el Módulo 37.")

elif opcion == "35: Razonamiento":
    import modulo_35
    modulo_35.ejecutar()
elif opcion == "36: Buscador":
    import modulo_36
    modulo_36.ejecutar()
elif opcion == "37: Ingesta":
    import modulo_37
    modulo_37.ejecutar()
