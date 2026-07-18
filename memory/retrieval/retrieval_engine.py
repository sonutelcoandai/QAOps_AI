from memory.memory_manager import MemoryManager


class RetrievalEngine:
    @staticmethod
    def retrieve(query, limit=5):

        results = MemoryManager.search(query)

        return results[:limit]
