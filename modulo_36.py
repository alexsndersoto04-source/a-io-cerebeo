import streamlit as st
import requests

def ejecutar():
    st.header("🔍 Rastreador A IO (Wikipedia Directa)")
    st.write("Consulta en tiempo real a la base de conocimiento global.")

    query = st.text_input("Ingresa el término que desees buscar:")
    
    if query:
        with st.spinner(f"Extrayendo conocimiento sobre '{query}'..."):
            # Conectamos directamente con la API de Wikipedia en español
            S = requests.Session()
            URL = "https://es.wikipedia.org/w/api.php"

            PARAMS = {
                "action": "query",
                "format": "json",
                "titles": query,
                "prop": "extracts",
                "exintro": True,
                "explaintext": True,
            }

            try:
                R = S.get(url=URL, params=PARAMS)
                DATA = R.json()
                PAGES = DATA["query"]["pages"]
                
                # Extraemos el contenido
                page_id = next(iter(PAGES))
                if page_id != "-1":
                    contenido = PAGES[page_id]["extract"]
                    st.success(f"✅ Conocimiento Localizado para: {query}")
                    st.write(contenido)
                else:
                    st.warning(f"No hay información exacta para '{query}'. Intenta con otro término.")
            
            except Exception as e:
                st.error(f"Error de conexión con el cerebro global: {e}")

if __name__ == "__main__":
    ejecutar()
