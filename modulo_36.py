import streamlit as st
import urllib.parse
import importlib

# Configuración para el rendimiento de tu Xiaomi Redmi 9C
st.set_page_config(page_title="A IO - Sistema Unificado", layout="centered")

def main():
    st.sidebar.title("🤖 A IO: Control Total")
    
    # 1. Definimos la lista de módulos
    # Esto crea automáticamente las opciones del 01 al 35
    opciones = [f"Módulo {str(i).zfill(2)}" for i in range(1, 36)]
    opciones.append("Módulo 36: Enlace Neuronal (Cerebro)")

    seleccion = st.sidebar.selectbox("Selecciona Dimensión Cognitiva:", opciones)
    st.sidebar.markdown("---")

    # --- LÓGICA DE CARGA DINÁMICA ---

    if "Cerebro" in seleccion:
        # --- MÓDULO 36: CONEXIÓN AL CEREBRO ---
        st.title("🧠 Módulo 36: Enlace Neuronal")
        st.info("Conexión activa con el cerebro de datos externo.")
        
        concepto = st.text_input("Ingresa el término para investigación:")
        
        if concepto:
            query_safe = urllib.parse.quote(concepto)
            # Asegúrate de que esta URL sea la de tu app de cerebro
            url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"
            
            st.markdown(f"""
                <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                    <div style="padding:20px; background-color:#4CAF50; color:white; text-align:center; border-radius:10px; font-weight:bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                        🚀 SINCRONIZAR CEREBRO: {concepto.upper()}
                    </div>
                </a>
            """, unsafe_allow_html=True)
            st.caption("Nota: Se abrirá en una pestaña nueva para proteger tu memoria RAM.")

    else:
        # --- MÓDULOS 01 AL 35: CARGA AUTOMÁTICA ---
        # Convertimos "Módulo 01" en "modulo_01" para buscar el archivo
        id_modulo = seleccion.lower().replace(" ", "_")
        
        try:
            # Intentamos cargar el archivo .py correspondiente
            modulo = importlib.import_module(id_modulo)
            # Ejecutamos su función principal
            modulo.ejecutar()
        except ImportError:
            st.error(f"⚠️ Error: No se encuentra el archivo `{id_modulo}.py` en tu repositorio.")
        except Exception as e:
            st.error(f"❌ Error crítico en {seleccion}: {e}")

if __name__ == "__main__":
    main()
