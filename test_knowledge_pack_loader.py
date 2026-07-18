from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

from knowledge.knowledge_pack_loader import KnowledgePackLoader

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

load_memory_providers()

MemoryManager.initialize()

result = KnowledgePackLoader.load_all()

print(result)
