# Multi-LLM Agent

Agente en Python con LangChain que permite alternar entre distintos modelos LLM (OpenAI, Gemini, Claude) cambiando solo una variable.

## 🚀 Uso
1. Crear archivo `.env` con tus API keys.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
3. Ejecutar con uno de los comandos:
   python main.py gemini ->usa gemini-2.5-flash
   python main.py openai ->usa gpt-4o-mini
   python main.py anthropic ->usa claude-3-haiku-20240307
