# 🤖 Chatbot con Llama-3.3-70b-versatile (Groq + LangChain + Streamlit)

Esta aplicación implementa un **agente conversacional** utilizando el modelo **Llama3-8B** desplegado en **Groq Cloud**, con interfaz de chat en **Streamlit** y memoria conversacional gracias a **LangChain**.

El objetivo es ofrecer una experiencia de chat interactiva, manteniendo el contexto de la conversación y mostrando el historial de mensajes.

---

## ✨ Características principales

- 🚀 **Interfaz web con Streamlit** para un chat simple e intuitivo.  
- 🧠 **Modelo Llama-3.3-70b-versatile** corriendo en **Groq Cloud**.  
- 🔗 **LangChain** para la orquestación de cadenas y manejo de memoria conversacional.  
- 💾 **Memoria persistente en sesión**: el chat recuerda lo que has dicho durante la sesión.  
- ⚡ **Respuestas rápidas** gracias a la aceleración de Groq.  

---

## 📂 Estructura del proyecto

```bash
.
├── app.py                # Interfaz de usuario con Streamlit
├── utils/
│   └── agent_setup.py    # Configuración del agente conversacional
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
