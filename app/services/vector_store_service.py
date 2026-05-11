from app.services.ingestion_service import IngestionService


class VectorStoreService:

    def __init__(self):

        self.ingestion_service = IngestionService()

    def get_status(self):

        documents = self.ingestion_service.load_sample_documents()

        return {
            "vector_store": "faiss",
            "documents_loaded": len(documents),
            "status": "ready_for_indexing"
        }