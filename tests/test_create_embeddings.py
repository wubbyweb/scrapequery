
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_embeddings():
    response = client.post("/api/v1/create-embeddings")
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "Embeddings created successfully",
        "collection_name": "example_collection"
    }