# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with your API keys:
```
OPENAI_API_KEY=...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...
```

## Running the App

```bash
# Flask API on port 3000
python app.py

# Interactive CLI (provider hardcoded in main.py line 4)
python main.py

# Single-query test (quick validation)
python mainv1.py

# List available Gemini models
python ListarModelosGemini.py
```

Type `salir`, `exit`, or `quit` to end interactive CLI sessions.

## Flask API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/chat` | Send a message; returns the LLM response |
| `DELETE` | `/chat/<session_id>` | Clear a session's history |
| `GET` | `/providers` | List supported providers |

**POST /chat — body:**
```json
{ "message": "Hola", "provider": "gemini", "session_id": "abc123" }
```
`provider` (default `"gemini"`) and `session_id` (default `"default"`) are optional.
Each unique `session_id` keeps its own independent conversation history in memory.

## Architecture

The app is a single-provider-at-a-time LLM chat CLI using LangChain. The active provider is set by changing the `provider` string variable at the top of `main.py` or `mainv1.py`.

**Data flow:**
```
main.py  →  llm_provider.get_llm(provider)  →  LangChain ChatModel  →  LLM API
```

**Key module — [llm_provider.py](llm_provider.py):** Factory function `get_llm(provider: str)` returns the appropriate LangChain chat model instance (`"openai"` → `gpt-4o-mini`, `"gemini"` → `models/gemini-2.5-flash`, `"anthropic"` → `claude-3-haiku-20240307`).

**Conversation memory in [main.py](main.py):** A plain Python list `chat_history` accumulates `HumanMessage` and `AIMessage` objects and is passed wholesale to the LLM on every turn — there is no LangChain memory abstraction, just manual list management.

**[mainv1.py](mainv1.py)** is a minimal script with no history, useful only for smoke-testing a provider.
