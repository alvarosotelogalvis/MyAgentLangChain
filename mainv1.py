from langchain_core.messages import HumanMessage
from llm_provider import get_llm

# Cambia aquí el proveedor: "openai", "gemini", "anthropic"
provider = "gemini"

llm = get_llm(provider)

response = llm.invoke([HumanMessage(content="Que es el sistema solar.")])
print(f"[{provider.upper()}] → {response.content}")

