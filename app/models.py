
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

class CreateEmbeddingsResponse(BaseModel):
    status: str
    message: str
    collection_name: str