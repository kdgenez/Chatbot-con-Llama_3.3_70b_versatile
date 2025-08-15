import streamlit as st
from utils.agent_setup import create_agent

# Configuración de la página
st.set_page_config(
    page_title="Agente Llama3-8b",
    page_icon="🤖",
    layout="centered"
)

# Inicialización del agente en session_state
if "agent" not in st.session_state:
    st.session_state.agent = create_agent()
    st.session_state.chat_history = []

# Interfaz de usuario
st.title("💬 Chat con Llama3-8b")
st.caption("Agente conversacional usando Llama3-8b-8192 via Groq")

# Mostrar historial de chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Manejo de entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta..."):
    # Agregar mensaje de usuario al historial
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtener respuesta del agente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.agent.predict(input=prompt)
            st.markdown(response)
    
    # Guardar respuesta en historial
    st.session_state.chat_history.append({"role": "assistant", "content": response})
