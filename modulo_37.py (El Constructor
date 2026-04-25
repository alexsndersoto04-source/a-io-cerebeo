import streamlit as st
import os
import requests
import json

def ejecutar():
    st.header("⚙️ Módulo 37: Pipeline de Ingesta y Aprendizaje")
    st.info("Este módulo descarga los 5GB de Wikipedia y extrae el conocimiento.")

    if not os.path.exists("data"):
        os.makedirs("data")

    # URL sugerida para el corpus en español (TXT plano)
    url_defecto = "https://raw.githubusercontent.com/stanleyfoster/spanish-corpus/master/spanish65mb.txt"
    url_corpus = st.text_input("URL del Corpus (TXT):", url_defecto)
    
    if st.button("📥 Iniciar Ciclo de Adquisición"):
        with st.status("Procesando...", expanded=True) as status:
            try:
                # PASO 1: Descarga por bloques (Streaming) para no saturar RAM
                status.write("Descargando archivo al servidor...")
                r = requests.get(url_corpus, stream=True)
                with open("data/wikipedia.txt", 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024*1024):
                        if chunk: f.write(chunk)
                
                # PASO 2: Aprendizaje (Indexación Semántica)
                status.write("Adquiriendo conocimiento (Indexando)...")
                indice = {}
                with open("data/wikipedia.txt", "r", encoding="utf-8") as f:
                    for i, linea in enumerate(f):
                        palabras = linea.lower().split()
                        for p in palabras[:10]: # Indexamos las primeras 10 palabras de cada párrafo
                            if len(p) > 5: # Solo palabras con significado
                                if p not in indice:
                                    indice[p] = i
                
                with open("data/mapa_conocimiento.json", "w") as f_json:
                    json.dump(indice, f_json)
                
                status.update(label="✅ Ciclo Completado: Conocimiento Adquirido", state="complete")
                st.success("A IO ahora tiene una base de datos de consulta.")
            except Exception as e:
                st.error(f"Error en el proceso: {e}")

if __name__ == "__main__":
    ejecutar()
