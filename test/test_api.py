import os
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture
def example_query():
    return {
        "user_id": "test_user",
        "query": "What's your cheapest product?"
    }

def test_query_endpoint_success(example_query):
    os.environ["TOP_K"] = "2"
    os.environ["PROMPT_FILE"] = "prompt.txt"  # debe existir y tener {context} y {query}

    response = client.post("/query", json=example_query)
    
    assert response.status_code == 200

    data = response.json()
    assert "answer" in data
    assert "docs_used" in data
    assert isinstance(data["docs_used"], list)
    assert len(data["docs_used"]) > 0
