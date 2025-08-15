import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def create_agent():
    """
    Crea el agente conversacional usando configuración de secrets.toml
    Versiones compatibles: langchain 0.1.16 + langchain-groq 0.1.3
    """
    llm = ChatGroq(
        groq_api_key=st.secrets.GROQ.API_KEY,
        model_name=st.secrets.AGENT.MODEL_NAME,
        temperature=st.secrets.AGENT.TEMPERATURE,
        max_tokens=st.secrets.AGENT.MAX_TOKENS
    )
    
    memory = ConversationBufferMemory()
    return ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
