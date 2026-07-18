from pathlib import Path
import sys
from knowledge.knowledge_search import KnowledgeSearch

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

MemoryManager.initialize()

MemoryManager.save("tmf641", "Service Order Management API")

MemoryManager.save("tmf620", "Product Catalog API")

results = KnowledgeSearch.search("Order")

print(results)
