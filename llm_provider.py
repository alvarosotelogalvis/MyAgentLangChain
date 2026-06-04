import os
from dotenv import load_dotenv

# Importaciones actualizadas según la nueva estructura de LangChain
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

def get_llm(provider: str):
    """
    Retorna el modelo LLM según el proveedor seleccionado.
    Proveedores soportados: "openai", "gemini", "anthropic".
    """
    if provider == "openai":
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    elif provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="models/gemini-2.5-flash",   # nombre exacto del modelo
            api_key=os.getenv("GEMINI_API_KEY")
        )
    elif provider == "anthropic":
        return ChatAnthropic(
            model="claude-3-haiku-20240307",
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
    else:
        raise ValueError(f"Proveedor no soportado: {provider}")
