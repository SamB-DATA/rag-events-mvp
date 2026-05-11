from app.services.vector_store_service import VectorStoreService


class RagService:

    def __init__(self):

        self.vector_store_service = VectorStoreService()

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

        answer_lines = []

        for document in documents:

            line = (
                f"- {document.title} à {document.location} "
                f"le {document.date}"
            )

            answer_lines.append(line)

        final_answer = (
            "Voici les événements les plus pertinents :\n\n"
            + "\n".join(answer_lines)
        )

        return {
            "query": query,
            "answer": final_answer,
            "sources": documents
        }