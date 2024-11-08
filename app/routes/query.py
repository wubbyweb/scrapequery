
from fastapi import APIRouter
from app.models import QueryRequest, QueryResponse
from app.services import embedding_service, storage_service

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    query_embedding = embedding_service.create_embeddings(request.query)
    matched_content = storage_service.match_embeddings(query_embedding)
    answer = embedding_service.generate_answer(matched_content)
    
    return {"answer": answer}