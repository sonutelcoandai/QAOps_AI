from pathlib import Path
import sys
from memory.embeddings.embedding_service import EmbeddingService

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


vector = EmbeddingService.generate_embedding("TMF641 Service Order API")

print(vector)

embedding1 = EmbeddingService.generate_embedding("TMF641")

embedding2 = EmbeddingService.generate_embedding("TMF641")

print(embedding1 == embedding2)

embedding1 = EmbeddingService.generate_embedding("TMF641")

embedding2 = EmbeddingService.generate_embedding("TMF620")

print(embedding1 == embedding2)
