import streamlit as st
import urllib.parse
import os

# Configuración de rendimiento para el Redmi 9C
st.set_page_config(page_title="A IO - Sistema Integrado", layout="centered")

def main():
    st.sidebar.title("🤖 A IO: Panel Central")
    
    # 1. Definimos las opciones del menú
    # Mantenemos tus 35 dimensiones y añadimos el Cerebro
    opciones = [f"Dimensión {i}" for i in range(1, 36)]
    opciones.append("Módulo 36: Enlace al Cerebro")
    
    seleccion = st.sidebar.selectbox("Selecciona un Módulo:", opciones)
    st.sidebar.markdown("---")
    st.sidebar.caption("Alexander Soto | A IO Project")

    # --- LÓGICA DE INTEGRACIÓN ---

    if seleccion == "Módulo 36: Enlace al Cerebro":
        # Este es el código nuevo que conecta con tu segunda app
        st.title("🧠 Módulo 36: Enlace Neuronal")
        st.write("Puente de datos hacia el Cerebro externo (Wikipedia API).")
        
        concepto = st.text_input("Ingresa el concepto para investigación:")
        
        if concepto:
            query_safe = urllib.parse.quote(concepto)
            # URL de tu app de cerebro (basada en tu captura)
            url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"
            
            st.markdown(f"""
                <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                    <div style="padding:20px; background-color:#4CAF50; color:white; text-align:center; border-radius:10px; font-weight:bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                        🚀 SINCRONIZAR CON CEREBRO: {concepto.upper()}
                    </div>
                </a>
            """, unsafe_allow_html=True)
            st.info("Nota: Se abrirá en una pestaña nueva para ahorrar memoria RAM.")

    else:
        # --- CARGA DE TUS 35 MÓDULOS ACTUALES ---
        st.title(f"📂 {seleccion}")
        
        # Aquí no tocamos tus archivos. El sistema simplemente te dice 
        # que puedes seguir usando la lógica que ya tenías programada.
        st.write("Lógica de procesamiento activa para esta dimensión.")
        
        # Alexander, aquí es donde tú ya tienes tus 'if' o llamadas 
        # a los otros módulos. Simplemente no los borres.
        st.warning("Usa el menú lateral para saltar al Módulo 36 cuando necesites datos de Wikipedia.")

if __name__ == "__main__":
    main()
