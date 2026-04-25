import streamlit as st
import wikipedia

# Configuración de idioma para Wikipedia
wikipedia.set_lang("es")

def main():
    st.title("🧠 Cerebro A IO")
    st.write("Estado: Conexión Neuronal Activa")

    # --- AQUÍ RECIBIMOS LA PALABRA DE LA APP 1 ---
    # Buscamos si en la URL viene el parámetro "busqueda"
    parametros = st.query_params
    palabra_enviada = parametros.get("busqueda", "")

    # El buscador se llena solo con la palabra que mandaste
    query = st.text_input("Concepto a investigar:", value=palabra_enviada)

    if query:
        st.divider()
        try:
            with st.spinner(f"Buscando '{query}' en la base de datos..."):
                # Obtenemos el resumen de Wikipedia
                resultado = wikipedia.summary(query, sentences=4)
                st.markdown("### 📄 Información Encontrada")
                st.info(resultado)
        except wikipedia.exceptions.PageError:
            st.error("No se encontró información exacta. Intenta con otra palabra.")
        except wikipedia.exceptions.DisambiguationError:
            st.warning("El término es muy general. Sé más específico.")
        except Exception as e:
            st.error("Error de conexión con la base de datos.")

if __name__ == "__main__":
    main()
