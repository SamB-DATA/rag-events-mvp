from app.models.document import EventDocument


class IngestionService:

    def load_sample_documents(self) -> list[EventDocument]:

        return [
            EventDocument(
                id="event_001",
                title="Festival de jazz à Paris",
                description="Un festival de jazz avec plusieurs artistes internationaux.",
                location="Paris",
                date="2026-06-15",
                source="sample"
            ),
            EventDocument(
                id="event_002",
                title="Exposition d’art contemporain",
                description="Une exposition autour de l’art moderne et des installations numériques.",
                location="Lyon",
                date="2026-07-02",
                source="sample"
            )
        ]