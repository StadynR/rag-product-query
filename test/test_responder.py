from src.agents import ResponderAgent

def test_generate_response_from_context():
    prompt = "Given the context:\n{context}\nanswer to the querya:\n{query}"

    context_docs = [
        "Product A is available in blue and red.",
        "Product B is available in green and black."
    ]
    query = "What colors are available for Product A?"

    responder = ResponderAgent(prompt)
    response = responder.generate(query, context_docs)

    assert isinstance(response, str)
    assert len(response) > 0
    assert "blue" in response.lower() or "red" in response.lower()
