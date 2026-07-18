from memory.retrieval.retrieval_engine import RetrievalEngine


class KnowledgeSearch:
    @staticmethod
    def search(query, limit=5):

        return RetrievalEngine.retrieve(query=query, limit=limit)
