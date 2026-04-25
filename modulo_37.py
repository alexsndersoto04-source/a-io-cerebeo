import streamlit as st
import os, requests, json

def ejecutar():
    st.header("⚙️ Módulo 37: Ingesta de Conocimiento")
    if not os.path.exists("data"): os.makedirs("data")

    url = "https://raw.githubusercontent.com/stanleyfoster/spanish-corpus/master/spanish65mb.txt"
    
    if st.button("📥 INICIAR APRENDIZAJE TOTAL"):
        with st.status("Adquiriendo conocimiento...", expanded=True) as s:
            r = requests.get(url, stream=True)
            with open("data/wikipedia.txt", 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk: f.write(chunk)
            
            s.write("Creando Mapa Semántico...")
            indice = {}
            with open("data/wikipedia.txt", "r", encoding="utf-8") as f:
                for i, linea in enumerate(f):
                    palabras = linea.lower().split()
                    for p in palabras:
                        if len(p) > 3: # Indexa todas las palabras de más de 3 letras
                            if p not in indice: indice[p] = i
            
            with open("data/mapa_conocimiento.json", "w") as f_j:
                json.dump(indice, f_j)
            s.update(label="✅ MEMORIA SINCRONIZADA", state="complete")
