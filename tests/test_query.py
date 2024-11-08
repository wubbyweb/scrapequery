
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query():
    response = client.post("/api/v1/query", json={"query": "What is the capital of France?"})
    assert response.status_code == 200
    assert "answer" in response.json()