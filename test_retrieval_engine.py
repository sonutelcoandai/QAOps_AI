from pathlib import Path
import sys

from memory.memory_manager import MemoryManager

from memory.retrieval.retrieval_engine import RetrievalEngine

from memory_providers.load_memory_providers import load_memory_providers

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

MemoryManager.initialize()

MemoryManager.save("tmf641", "Service Order Management API")

MemoryManager.save("tmf620", "Product Catalog API")

results = RetrievalEngine.retrieve("Order")

print(results)
