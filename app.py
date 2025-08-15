import streamlit as st
from utils.agent_setup import create_agent

# Configuración estable de la página
st.set_page_config(
    page_title="🤖 Agente Llama3-8b",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inicialización segura del agente
def init_agent():
    if "agent" not in st.session_state:
        st.session_state.agent = create_agent()
        st.session_state.messages = [{"role": "assistant", "content": "¡Hola! Soy Llama3-8b, ¿en qué puedo ayudarte?"}]

init_agent()

# Interfaz de chat optimizada
st.title("💬 Chat con Llama3-8b")
st.caption("Powered by Groq Cloud - llama3-8b-8192 model")

# Mostrar historial de mensajes
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Procesamiento de inputs del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Agregar mensaje de usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Generar respuesta con el agente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = st.session_state.agent.predict(input=prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
