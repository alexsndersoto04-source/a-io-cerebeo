import streamlit as st
import urllib.parse

# 1. Configuración de la aplicación
st.set_page_config(page_title="A IO - Sistema Integrado", layout="centered")

def main():
    st.sidebar.title("🤖 A IO: Panel Control")
    
    # --- AQUÍ ESTÁ EL TRUCO PARA QUE APAREZCA ---
    # Creamos la lista del 1 al 35
    opciones = [f"Dimensión {i}" for i in range(1, 36)]
    
    # AHORA INTEGRAMOS EL 36 MANUALMENTE PARA QUE SALGA EN EL MENÚ
    opciones.append("Módulo 36: Enlace al Cerebro")

    # Mostramos el menú con todas las opciones (1 al 36)
    seleccion = st.sidebar.selectbox("Selecciona un Módulo:", opciones)
    st.sidebar.markdown("---")

    # --- LÓGICA DE VISUALIZACIÓN ---

    if seleccion == "Módulo 36: Enlace al Cerebro":
        # ESTE ES EL MÓDULO QUE SE CONECTA AL CEREBRO
        st.title("🧠 Módulo 36: Enlace Neuronal")
        st.write("Escribe el concepto que quieres que la IA investigue en el cerebro.")

        concepto = st.text_input("Término de búsqueda:")

        if concepto:
            # Preparamos la URL para el salto entre apps
            query_safe = urllib.parse.quote(concepto)
            url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"
            
            st.success(f"Listo para sincronizar: {concepto}")
            
            st.markdown(f"""
                <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                    <div style="padding:15px; background-color:#4CAF50; color:white; text-align:center; border-radius:10px; font-weight:bold;">
                        🚀 ABRIR CEREBRO Y BUSCAR: {concepto.upper()}
                    </div>
                </a>
            """, unsafe_allow_html=True)

    else:
        # AQUÍ SE MUESTRAN TUS OTROS 35 MÓDULOS
        st.title(f"📂 {seleccion}")
        st.info("Cargando lógica interna de la dimensión...")
        # Aquí es donde va el código que ya tenías para tus 35 módulos
        # No lo borres, simplemente déjalo debajo de este bloque.

if __name__ == "__main__":
    main()
