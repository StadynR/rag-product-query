from src.agents import ResponderAgent

def test_generate_response_from_context():
    prompt = "Dado el siguiente contexto:\n{context}\nresponde a la consulta:\n{query}"

    context_docs = [
        "El Producto A está disponible en color azul y rojo.",
        "El Producto B tiene opciones verdes y negras."
    ]
    query = "¿Qué colores tiene el Producto A?"

    responder = ResponderAgent(prompt)
    response = responder.generate(query, context_docs)

    assert isinstance(response, str)
    assert len(response) > 0
    assert "azul" in response.lower() or "rojo" in response.lower()
