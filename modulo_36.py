import streamlit as st
import requests

def ejecutar():
    st.header("🔍 Rastreador A IO (Enlace Activo)")
    
    # --- CAPTURA DE DATOS EXTERNOS ---
    # Revisamos si la App Principal envió una búsqueda por la URL
    params = st.query_params
    busqueda_externa = params.get("busqueda", "")
    
    # Si hay búsqueda externa, la usamos; si no, dejamos el campo vacío
    query = st.text_input("Concepto a investigar:", value=busqueda_externa)
    
    if query:
        with st.spinner(f"Consultando conocimiento global sobre '{query}'..."):
            url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            headers = {"User-Agent": "A-IO-Project/1.0"}
            
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Datos sincronizados con el Cuerpo")
                    st.write(data.get("extract", "No hay resumen disponible."))
                else:
                    st.warning("El término no se encontró o la conexión es inestable.")
            except Exception as e:
                st.error(f"Error de enlace: {e}")

if __name__ == "__main__":
    ejecutar()
