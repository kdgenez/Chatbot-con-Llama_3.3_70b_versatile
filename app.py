import streamlit as st
from utils.agent_setup import create_agent

st.set_page_config(
    page_title="🤖 Agente Llama3-8b",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def init_agent():
    if "agent" not in st.session_state:
        st.session_state.agent = create_agent()
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "¡Hola! Soy Llama3-8b, ¿en qué puedo ayudarte?"}]

init_agent()

st.title("💬 Chat con Llama3-8b")
st.caption("Powered by Groq Cloud - llama3-8b-8192 model")

# Mostrar historial
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Procesamiento de inputs
if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = st.session_state.agent.run(prompt)  # 🔥 corrección aquí
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

