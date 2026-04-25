import streamlit as st
import requests

def ejecutar():
    st.header("🔍 Módulo 36: Rastreador en Tiempo Real")
    query = st.text_input("Ingresa término:").strip().lower()
    
    if query:
        url = "https://raw.githubusercontent.com/stanleyfoster/spanish-corpus/master/spanish65mb.txt"
        with st.spinner(f"Buscando '{query}' en la base de datos central..."):
            try:
                # Leemos el archivo línea por línea directamente desde la URL
                response = requests.get(url, stream=True)
                encontrado = False
                
                # Solo revisamos las primeras 5000 líneas para que tu Xiaomi no sufra
                for i, line in enumerate(response.iter_lines(decode_unicode=True)):
                    if i > 5000: break 
                    if query in line.lower():
                        st.success(f"✅ ¡Dato localizado!")
                        st.info(f"INFORMACIÓN ENCONTRADA: {line}")
                        encontrado = True
                        break
                
                if not encontrado:
                    st.warning("El término no aparece en las primeras muestras del corpus.")
            except Exception as e:
                st.error(f"Error de conexión: {e}")

if __name__ == "__main__":
    ejecutar()
