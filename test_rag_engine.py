from pathlib import Path
import sys
from knowledge.knowledge_ingestion import KnowledgeIngestion

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

from orchestration.provider_manager import ProviderManager

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.fallback.fallback_manager import FallbackManager

from ai_providers.load_providers import load_providers

from memory.retrieval.rag_engine import RAGEngine

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()
MemoryManager.initialize()

KnowledgeIngestion.ingest("knowledge/tmforum/tmf641.md")

ProviderManager.load()
load_providers()

ModelRegistry.load()
RoutingPolicy.load()
FallbackManager.load()

result = RAGEngine.answer("What is Service Order?")

print(result)
