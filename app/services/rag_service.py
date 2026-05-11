from app.services.llm_service import LLMService
from app.services.vector_store_service import VectorStoreService


class RagService:

    def __init__(self):

        self.vector_store_service = VectorStoreService()
        self.llm_service = LLMService()

    def answer_query(self, query: str, top_k: int = 2):

        search_results = self.vector_store_service.search(
            query=query,
            top_k=top_k
        )

        results = search_results["results"]

        if not results:

            return {
                "query": query,
                "answer": "Aucun événement pertinent trouvé.",
                "sources": []
            }

        documents = [
            result["document"]
            for result in results
        ]

        context_lines = []

        for document in documents:

            line = (
                f"Titre : {document.title}\n"
                f"Description : {document.description}\n"
                f"Lieu : {document.location}\n"
                f"Date : {document.date}\n"
                f"Source : {document.source}\n"
            )

            context_lines.append(line)

        context = "\n---\n".join(context_lines)

        answer = self.llm_service.generate_answer(
            question=query,
            context=context
        )

        return {
            "query": query,
            "answer": answer,
            "sources": documents
        }