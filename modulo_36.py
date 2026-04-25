import streamlit as st
import urllib.parse
import importlib

# 1. Configuración de pantalla para el Xiaomi Redmi 9C
st.set_page_config(page_title="A IO - Sistema Completo", layout="centered")

def main():
    st.sidebar.title("🤖 A IO: Panel de Control")
    
    # --- LISTA DE MÓDULOS (Respetamos los 35 actuales) ---
    # Creamos la lista del 1 al 35
    opciones = [f"Módulo {str(i).zfill(2)}" for i in range(1, 36)]
    # Añadimos el nuevo módulo al final de la lista
    opciones.append("Módulo 36: Enlace Neuronal")

    seleccion = st.sidebar.selectbox("Selecciona una Dimensión:", opciones)

    # --- LÓGICA DE INTEGRACIÓN TOTAL ---

    if seleccion == "Módulo 36: Enlace Neuronal":
        # CÓDIGO DEL MÓDULO 36 (Incrustado para evitar errores de archivo)
        st.title("🧠 Módulo 36: Enlace Neuronal")
        st.write("Puente cognitivo hacia el Cerebro de Datos externo.")
        
        concepto = st.text_input("Ingresa el concepto a investigar:")
        
        if concepto:
            query_safe = urllib.parse.quote(concepto)
            url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"
            
            st.markdown(f"""
                <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                    <div style="padding:20px; background-color:#4CAF50; color:white; text-align:center; border-radius:10px; font-weight:bold; box-shadow: 2px 2px 10px rgba(0,0,0,0.3);">
                        🚀 SINCRONIZAR CON CEREBRO: {concepto.upper()}
                    </div>
                </a>
            """, unsafe_allow_html=True)
            st.caption("Se abrirá una nueva pestaña para no saturar la RAM de tu Xiaomi.")

    else:
        # --- ESTO MANTIENE TUS 35 MÓDULOS TRABAJANDO ---
        st.title(f"📂 {seleccion}")
        
        # Generamos el nombre del archivo basado en la selección (ej: modulo_01.py)
        nombre_modulo = seleccion.lower().replace(" ", "_").replace("ó", "o")
        
        try:
            # Importamos el módulo dinámicamente sin que se rompa la app
            modulo_externo = importlib.import_module(nombre_modulo)
            # Ejecutamos la función principal de tus módulos antiguos
            modulo_externo.ejecutar() 
        except ImportError:
            st.error(f"No se encontró el archivo `{nombre_modulo}.py`. Asegúrate de que esté en tu GitHub.")
        except AttributeError:
            st.error(f"El archivo `{nombre_modulo}.py` no tiene una función llamada `ejecutar()`.")
        except Exception as e:
            st.error(f"Error al cargar el módulo: {e}")

if __name__ == "__main__":
    main()
