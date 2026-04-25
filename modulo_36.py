import streamlit as st
import json
import linecache

def ejecutar():
    st.header("🔍 Módulo 36: Rastreador de Conocimiento")
    st.write("Localiza información en milisegundos dentro del corpus.")

    query = st.text_input("Ingresa término de búsqueda:").lower()
    
    if query:
        if os.path.exists("data/mapa_conocimiento.json"):
            with open("data/mapa_conocimiento.json", "r") as f:
                indice = json.load(f)
            
            if query in indice:
                linea_num = indice[query]
                # Leemos la línea exacta sin cargar todo el archivo
                resultado = linecache.getline("data/wikipedia.txt", linea_num + 1)
                st.success(f"Dato localizado en Línea {linea_num}:")
                st.info(resultado)
            else:
                st.warning("El término no existe en el conocimiento actual.")
        else:
            st.error("Error: Primero activa el Módulo 37 para aprender.")

if __name__ == "__main__":
    import os
    ejecutar()
