import pytest
from src.agents import RetrieverAgent

@pytest.fixture(scope="module")
def retriever():
    return RetrieverAgent()

def test_retrieve_returns_results(retriever):
    query = "What products are red?"
    results = retriever.retrieve(query, top_k=2)
    
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(doc, str) for doc in results)
