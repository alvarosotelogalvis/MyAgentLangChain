from langchain_core.messages import HumanMessage, AIMessage
from llm_provider import get_llm

provider = "gemini"  # Cambia entre "openai", "gemini", "anthropic"
llm = get_llm(provider)

print(f"🤖 Agente multi-LLM iniciado con {provider.upper()}. Escribe 'salir' para terminar.\n")

# Historial de conversación
chat_history = []

while True:
    user_input = input("Tú: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Conversación terminada.")
        break

    # Agregar mensaje del usuario al historial
    chat_history.append(HumanMessage(content=user_input))

    # Pasar todo el historial al modelo
    response = llm.invoke(chat_history)

    # Mostrar respuesta
    print(f"{provider.upper()}: {response.content}\n")

    # Agregar respuesta del modelo al historial
    chat_history.append(AIMessage(content=response.content))
