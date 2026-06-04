from flask import Flask, request, jsonify, render_template
from langchain_core.messages import HumanMessage, AIMessage
from llm_provider import get_llm

app = Flask(__name__)

# Historial por sesión: { session_id: { "llm": ..., "history": [...], "provider": ... } }
sessions = {}


@app.get("/")
def index():
    return render_template("index.html")


def get_or_create_session(session_id: str, provider: str):
    if session_id not in sessions or sessions[session_id]["provider"] != provider:
        sessions[session_id] = {
            "provider": provider,
            "llm": get_llm(provider),
            "history": [],
        }
    return sessions[session_id]


@app.post("/chat")
def chat():
    """
    Body JSON:
      { "message": "Hola", "provider": "gemini", "session_id": "abc123" }
    provider y session_id son opcionales (defaults: gemini / default).
    """
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "El campo 'message' es requerido"}), 400

    provider = data.get("provider", "gemini")
    session_id = data.get("session_id", "default")

    try:
        session = get_or_create_session(session_id, provider)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    session["history"].append(HumanMessage(content=message))
    response = session["llm"].invoke(session["history"])
    session["history"].append(AIMessage(content=response.content))

    return jsonify({
        "response": response.content,
        "provider": provider,
        "session_id": session_id,
    })


@app.delete("/chat/<session_id>")
def clear_session(session_id: str):
    """Elimina el historial de una sesión."""
    sessions.pop(session_id, None)
    return jsonify({"message": f"Sesión '{session_id}' eliminada"})


@app.get("/providers")
def list_providers():
    """Lista los proveedores disponibles."""
    return jsonify({"providers": ["openai", "gemini", "anthropic"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
