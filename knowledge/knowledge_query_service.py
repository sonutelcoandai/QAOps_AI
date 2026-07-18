from memory.retrieval.rag_engine import RAGEngine


class KnowledgeQueryService:
    @staticmethod
    def ask(question):

        return RAGEngine.answer(question)
