from pathlib import Path

import faiss
import numpy as np

from app.services.embedding_service import EmbeddingService
from app.services.ingestion_service import IngestionService


class VectorStoreService:

    def __init__(self):

        self.ingestion_service = IngestionService()
        self.embedding_service = EmbeddingService()

        self.index_path = "vector_store/faiss.index"

    def build_index(self):

        documents = self.ingestion_service.load_documents()

        texts = [
            f"{doc.title} {doc.description}"
            for doc in documents
        ]

        embeddings = [
            self.embedding_service.create_embedding(text)
            for text in texts
        ]

        embeddings_array = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings_array.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings_array)

        faiss.write_index(index, self.index_path)

        return {
            "documents_indexed": len(documents),
            "embedding_dimension": dimension,
            "index_path": self.index_path,
            "status": "index_created"
        }

    def search(self, query: str, top_k: int = 2):

        if not Path(self.index_path).exists():
            raise FileNotFoundError(
                "L'index FAISS est introuvable. Lancez d'abord /rag/build-index."
            )

        documents = self.ingestion_service.load_documents()

        index = faiss.read_index(self.index_path)

        query_embedding = self.embedding_service.create_embedding(query)

        query_array = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = index.search(query_array, top_k)

        results = []

        for position, document_index in enumerate(indices[0]):

            if document_index == -1:
                continue

            document = documents[document_index]

            results.append(
                {
                    "rank": position + 1,
                    "score": float(distances[0][position]),
                    "document": document
                }
            )

        return {
            "query": query,
            "top_k": top_k,
            "results": results
        }

    def get_status(self):

        index_exists = Path(self.index_path).exists()

        return {
            "vector_store": "faiss",
            "index_exists": index_exists,
            "index_path": self.index_path
        }