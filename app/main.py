from fastapi import FastAPI

from app.core.settings import settings
from app.services.ingestion_service import IngestionService
from app.services.vector_store_service import VectorStoreService


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API du système RAG événements culturels"
)

ingestion_service = IngestionService()
vector_store_service = VectorStoreService()


@app.get("/")
def home():

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "message": "Bienvenue sur le MVP RAG Events"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@app.get("/config")
def get_config():

    return {
        "llm_model": settings.llm_model,
        "vector_store": settings.vector_store_path
    }


@app.get("/documents")
def get_documents():

    documents = ingestion_service.load_documents()

    return {
        "count": len(documents),
        "documents": documents
    }


@app.post("/rag/build-index")
def build_rag_index():

    return vector_store_service.build_index()


@app.get("/rag/status")
def rag_status():

    return vector_store_service.get_status()