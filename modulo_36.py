# --- DENTRO DE TU APP.PY PRINCIPAL ---
import streamlit as st
import urllib.parse

# ... (Tu código de configuración y menú lateral) ...

if seleccion == "Módulo 36: Enlace al Cerebro":
    # ESTO ES LO QUE DEBE APARECER SI NO ENCUENTRA EL ARCHIVO
    st.title("🧠 Enlace Neuronal A IO")
    st.markdown("---")
    st.write("Escribe el concepto que quieres que la IA investigue en el cerebro externo.")

    concepto = st.text_input("Término de búsqueda:", placeholder="Ejemplo: Robótica, Inteligencia Artificial...")

    if concepto:
        # Codificamos para que sea una URL válida
        query_safe = urllib.parse.quote(concepto)
        
        # Esta es la dirección de tu cerebro que ya funciona
        url_cerebro = f"https://a-io-cerebeo.streamlit.app/?busqueda={query_safe}"

        st.success(f"Listo para enviar: **{concepto}**")
        
        # Botón con estilo profesional
        st.markdown(f"""
            <a href="{url_cerebro}" target="_blank" style="text-decoration:none;">
                <div style="
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px;
                    text-align: center;
                    border-radius: 8px;
                    font-size: 18px;
                    font-weight: bold;
                    margin-top: 10px;
                    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
                ">
                    🚀 SINCRONIZAR CON CEREBRO
                </div>
            </a>
        """, unsafe_allow_html=True)
        st.caption("Al pulsar, se abrirá tu cerebro en una pestaña nueva para ahorrar RAM.")

elif seleccion == "Módulo 35": # Ejemplo de otro módulo
    st.title("Módulo 35")
    # Aquí iría el código del 35
