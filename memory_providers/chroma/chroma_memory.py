from memory_providers.base_memory import BaseMemory


class ChromaMemory(BaseMemory):
    def __init__(self):
        self.storage = {}

    def save(self, key, value):
        self.storage[key] = value

    def retrieve(self, key):
        return self.storage.get(key)

    def search(self, query):
        results = []

        query_words = query.lower().replace("?", "").split()

        for value in self.storage.values():
            if isinstance(value, dict):
                content = value.get("content", "")
            else:
                content = str(value)

            content = content.lower()

            for word in query_words:
                if word in content:
                    results.append(value)
                    break

        return results
