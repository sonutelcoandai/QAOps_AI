from pathlib import Path
import sys
from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

from knowledge.knowledge_ingestion import KnowledgeIngestion

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

MemoryManager.initialize()

KnowledgeIngestion.ingest("knowledge/tmforum/tmf641.md")

document = MemoryManager.retrieve("tmf641")

print(document)
