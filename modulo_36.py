import streamlit as st
import urllib.parse
import importlib

# Optimización para Xiaomi Redmi 9C (evitar recargas innecesarias)
st.set_page_config(page_title="A IO - Sistema Unificado", layout="centered")

def main():
    st.sidebar.title("🤖 A IO: Panel de Control")
    
    # 1. GENERACIÓN DINÁMICA DEL MENÚ (1 al 36)
    # Creamos la lista de opciones para que Streamlit las reconozca todas
    opciones = [f"Módulo {str(i).zfill(2)}" for i in range(1, 36)]
    opciones.append("Módulo 36: Enlace Neuronal")

    seleccion = st.sidebar.selectbox("Selecciona la Dimensión:", opciones)
    st.sidebar.markdown("---")

    # 2. LÓGICA DE INTEGRACIÓN DE MÓDULOS
    
    if seleccion == "Módulo 36: Enlace Neuronal":
        # --- MÓDULO 36: INTEGRADO COMO MÓDULO LÓGICO ---
        st.title("🧠 Módulo 36: Enlace Neuronal")
        st.write("Conector activo con el Cerebro de Datos Externo.")
        
        # Campo de entrada para la investigación
        concepto = st.text_input("Ingresa el concepto a investigar:", key="input_cerebro")
        
        if concepto:
            # Codificación de la búsqueda para la URL
            query_safe = urllib.parse.quote(concepto)
            # URL de tu aplicación de Cerebro
            url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"
            
            st.success(f"Sincronización lista para: {concepto.upper()}")
            
            # Botón de salto de aplicación
            st.markdown(f"""
                <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                    <div style="padding:20px; background-color:#4CAF50; color:white; text-align:center; border-radius:10px; font-weight:bold; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                        🚀 ACCEDER AL CEREBRO: {concepto.upper()}
                    </div>
                </a>
            """, unsafe_allow_html=True)
            st.caption("Se abrirá en una nueva pestaña para optimizar la RAM.")

    else:
        # --- INTEGRACIÓN DE LOS 35 MÓDULOS RESTANTES ---
        st.title(f"📂 {seleccion}")
        
        # Convertimos el nombre de la selección al nombre de tus archivos (ej: modulo_01)
        # Esto permite que tus 35 módulos sigan funcionando bajo su propia estructura
        nombre_modulo = seleccion.lower().replace(" ", "_")
        
        try:
            # Intentamos cargar el módulo desde tus subcarpetas
            # Nota: Aquí se asume que tus archivos están accesibles en el path de Python
            modulo_externo = importlib.import_module(nombre_modulo)
            modulo_externo.ejecutar()
        except ImportError:
            st.error(f"Archivo `{nombre_modulo}.py` no detectado. Revisa tus subcarpetas.")
        except Exception as e:
            st.error(f"Error en la ejecución del módulo: {e}")

if __name__ == "__main__":
    main()
