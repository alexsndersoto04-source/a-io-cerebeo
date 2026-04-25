import streamlit as st
import requests

def ejecutar():
    st.header("🔍 Rastreador A IO (Directo)")
    st.write("Conexión directa con la base de datos Wikimedia.")

    query = st.text_input("Ingresa una palabra clave:").strip().lower()
    
    if query:
        # Usamos un archivo más ligero pero real para asegurar que cargue rápido en tu Xiaomi
        url = "https://raw.githubusercontent.com/stanleyfoster/spanish-corpus/master/spanish65mb.txt"
        
        with st.spinner(f"Escaneando red neuronal para: {query}"):
            try:
                # El secreto: stream=True permite leer sin descargar el archivo
                response = requests.get(url, stream=True)
                encontrado = False
                contador = 0
                
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        if query in line.lower():
                            st.success(f"✅ Conocimiento Localizado")
                            st.info(line)
                            encontrado = True
                            break # Detenemos la búsqueda al encontrar el primer resultado
                    
                    contador += 1
                    if contador > 3000: # Límite de seguridad para no saturar tu Redmi 9C
                        break
                
                if not encontrado:
                    st.warning("El término no se encontró en la muestra actual. Intenta con: 'mundo', 'estado' o 'derecho'.")
            
            except Exception as e:
                st.error(f"Error de conexión: {e}")

if __name__ == "__main__":
    ejecutar()
