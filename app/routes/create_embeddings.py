
from fastapi import APIRouter
from app.models import CreateEmbeddingsResponse
from app.services import scraping_service, embedding_service, storage_service

router = APIRouter()

@router.post("/create-embeddings", response_model=CreateEmbeddingsResponse)
def create_embeddings():
    # Read URLs from config file
    urls = scraping_service.read_urls_from_config()
    
    # Process each URL
    for url in urls:
        content = scraping_service.scrape_content(url)
        embeddings = embedding_service.create_embeddings(content)
        storage_service.store_embeddings(embeddings)
    
    return {
        "status": "success",
        "message": "Embeddings created successfully",
        "collection_name": "example_collection"
    }