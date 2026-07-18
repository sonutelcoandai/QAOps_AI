from pathlib import Path
import sys

from knowledge.knowledge_ingestion import KnowledgeIngestion

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

MemoryManager.initialize()

KnowledgeIngestion.ingest("knowledge/tmforum/tmf641.md")

KnowledgeIngestion.ingest("knowledge/telecom/oss-basics.md")

print(MemoryManager.retrieve("tmf641"))

print(MemoryManager.retrieve("oss-basics"))
