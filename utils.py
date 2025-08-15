from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def create_agent():
    """
    Crea y configura el agente conversacional con Llama3
    usando las credenciales de Streamlit secrets.
    """
    llm = ChatGroq(
        groq_api_key=st.secrets["GROQ"]["API_KEY"],
        model_name=st.secrets["AGENT"]["MODEL_NAME"],
        temperature=st.secrets["AGENT"]["TEMPERATURE"],
        max_tokens=st.secrets["AGENT"]["MAX_TOKENS"]
    )
    
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    return conversation
