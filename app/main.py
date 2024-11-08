
from fastapi import FastAPI
from app.routes import create_embeddings, query

app = FastAPI()

app.include_router(create_embeddings.router, prefix="/api/v1")
app.include_router(query.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the scrapequery API"}