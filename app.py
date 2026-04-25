import streamlit as st

# 1. PROTECCIÓN DE LIBRERÍA: Esto evita que la app se caiga si falta wikipedia
try:
    import wikipedia
    BIBLIOTECA_LISTA = True
except ImportError:
    BIBLIOTECA_LISTA = False

# Configuración de interfaz para tu Xiaomi
st.set_page_config(page_title="Cerebro A IO", page_icon="🧠")

def main():
    st.title("🧠 Cerebro A IO")
    
    # Verificación de requisitos
    if not BIBLIOTECA_LISTA:
        st.error("⚠️ SISTEMA INCOMPLETO: Falta instalar la librería 'wikipedia'.")
        st.info("Por favor, crea el archivo **requirements.txt** en este repositorio y escribe: wikipedia")
        return

    # Configuración de idioma para la base de datos
    wikipedia.set_lang("es")
    st.write("🟢 **Estado:** Sincronización Neuronal Activa")

    # --- NÚCLEO DE CONEXIÓN CON APP PRINCIPAL ---
    # Capturamos lo que viene de la URL (el parámetro 'busqueda')
    parametros = st.query_params
    palabra_desde_principal = parametros.get("busqueda", "")

    st.markdown("---")
    
    # El cuadro de texto recibe automáticamente la palabra de la App Principal
    query = st.text_input("Concepto detectado por la IA:", value=palabra_enviada_limpia(palabra_desde_principal))

    if query:
        with st.status(f"Analizando '{query}'...", expanded=True) as status:
            try:
                # Buscamos en Wikipedia
                resumen = wikipedia.summary(query, sentences=4)
                st.markdown(f"### 📄 Memoria Extraída: {query.upper()}")
                st.success(resumen)
                status.update(label="Sincronización completa", state="complete")
            except wikipedia.exceptions.PageError:
                st.error("El concepto no existe en la base de datos de Wikipedia.")
            except wikipedia.exceptions.DisambiguationError:
                st.warning("Término ambiguo. Por favor, sé más específico.")
            except Exception as e:
                st.error("Error de comunicación con el servidor de datos.")

    # Pie de página técnico
    st.sidebar.title("A IO Network")
    st.sidebar.info("Cerebro conectado con App Principal A-IO-WEB")

def palabra_enviada_limpia(texto):
    """Limpia caracteres extraños si los hay"""
    if texto:
        return texto.strip()
    return ""

if __name__ == "__main__":
    main()
