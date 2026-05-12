from fastapi import FastAPI

from app.core.settings import settings
from app.models.chat import ChatQuery
from app.models.query import SearchQuery
from app.services.chat_service import ChatService
from app.services.ingestion_service import IngestionService
from app.services.rag_service import RagService
from app.services.vector_store_service import VectorStoreService


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API du système RAG événements culturels"
)

ingestion_service = IngestionService()
vector_store_service = VectorStoreService()
rag_service = RagService()
chat_service = ChatService()


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


@app.post("/rag/search")
def search_events(search_query: SearchQuery):

    return vector_store_service.search(
        query=search_query.query,
        top_k=search_query.top_k
    )


@app.post("/rag/answer")
def rag_answer(search_query: SearchQuery):

    return rag_service.answer_query(
        query=search_query.query,
        top_k=search_query.top_k
    )


@app.post("/rag/ask")
def rag_ask(search_query: SearchQuery):

    return rag_service.answer_query(
        query=search_query.query,
        top_k=search_query.top_k
    )


@app.post("/chat/ask")
def chat_ask(chat_query: ChatQuery):

    return chat_service.ask(
        session_id=chat_query.session_id,
        query=chat_query.query,
        top_k=chat_query.top_k
    )


@app.get("/chat/history/{session_id}")
def chat_history(session_id: str):

    return chat_service.get_history(session_id)


@app.delete("/chat/history/{session_id}")
def clear_chat_history(session_id: str):

    return chat_service.clear_history(session_id)