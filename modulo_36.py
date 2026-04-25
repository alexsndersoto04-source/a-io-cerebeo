import streamlit as st
import os, json, linecache

def ejecutar():
    st.header("🔍 Módulo 36: Rastreador de Conocimiento")
    query = st.text_input("Ingresa término:").strip().lower()
    
    if query:
        ruta_mapa = "data/mapa_conocimiento.json"
        if os.path.exists(ruta_mapa):
            with open(ruta_mapa, "r") as f:
                indice = json.load(f)
            
            if query in indice:
                linea_idx = indice[query]
                texto = linecache.getline("data/wikipedia.txt", linea_idx + 1)
                st.success(f"✅ Dato encontrado en la red neuronal")
                st.info(f"INFORMACIÓN: {texto}")
            else:
                st.warning(f"El término '{query}' no existe. Intenta con: 'españa', 'gobierno' o 'mundo'.")
        else:
            st.error("🚨 Mapa no encontrado. Ejecuta el Módulo 37 primero.")
