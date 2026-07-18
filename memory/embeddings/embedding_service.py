import hashlib


class EmbeddingService:
    @staticmethod
    def generate_embedding(text):

        text_hash = hashlib.sha256(text.encode()).hexdigest()

        embedding = []

        for i in range(0, 64, 8):
            embedding.append(int(text_hash[i : i + 8], 16))

        return embedding
