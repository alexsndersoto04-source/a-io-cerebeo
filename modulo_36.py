import streamlit as st
import os
import json
import linecache

def ejecutar():
    st.header("🔍 Módulo 36: Rastreador de Conocimiento")
    st.write("Localiza información en milisegundos dentro del corpus.")

    query_input = st.text_input("Ingresa término de búsqueda:")
    query = query_input.strip().lower()
    
    if query:
        # USAMOS EL NOMBRE CORRECTO: mapa_conocimiento.json
        ruta_mapa = "data/mapa_conocimiento.json"
        
        if os.path.exists(ruta_mapa):
            with open(ruta_mapa, "r") as f:
                indice = json.load(f)
            
            if query in indice:
                linea_num = indice[query]
                resultado = linecache.getline("data/wikipedia.txt", linea_num + 1)
                st.success(f"✅ ¡Dato localizado!")
                st.info(resultado)
            else:
                st.warning(f"El término '{query_input}' no está en el mapa.")
        else:
            st.error("🚨 Error: No se detecta 'mapa_conocimiento.json'. Ejecuta el Módulo 37 primero.")

if __name__ == "__main__":
    ejecutar()
