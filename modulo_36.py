import streamlit as st
import os
import json
import linecache

def ejecutar():
    st.header("🔍 Módulo 36: Rastreador de Conocimiento")
    st.write("Localiza información en milisegundos dentro del corpus.")

    # --- MEJORA DE INTEGRACIÓN ---
    # Usamos .strip() para quitar espacios accidentales y .lower() para las mayúsculas
    query_input = st.text_input("Ingresa término de búsqueda:")
    query = query_input.strip().lower()
    
    if query:
        if os.path.exists("data/mapa_knowledge.json"):
            with open("data/mapa_knowledge.json", "r") as f:
                indice = json.load(f)
            
            if query in indice:
                linea_num = indice[query]
                # Optimizamos la lectura: linecache es ultra rápido para archivos grandes
                resultado = linecache.getline("data/wikipedia.txt", linea_num + 1)
                
                st.success(f"✅ ¡Dato localizado!")
                st.markdown(f"**Resultado para '{query_input}':**")
                st.info(resultado)
            else:
                st.warning(f"El término '{query_input}' no está en el mapa. Prueba con palabras más generales.")
        else:
            st.error("🚨 Error: No se detecta el Mapa de Conocimiento. Ejecuta el Módulo 37 primero.")

if __name__ == "__main__":
    ejecutar()
