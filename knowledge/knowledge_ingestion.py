from pathlib import Path

from knowledge.document_loader import DocumentLoader

from memory.embeddings.embedding_service import EmbeddingService

from memory.memory_manager import MemoryManager


class KnowledgeIngestion:
    @staticmethod
    def ingest(file_path):

        content = DocumentLoader.load(file_path)

        embedding = EmbeddingService.generate_embedding(content)

        document_key = Path(file_path).stem

        MemoryManager.save(
            document_key,
            {"file": file_path, "content": content, "embedding": embedding},
        )

        return {"document": document_key, "status": "ingested"}
