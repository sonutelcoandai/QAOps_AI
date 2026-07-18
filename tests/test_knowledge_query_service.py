from pathlib import Path
import sys
from ai_providers.load_providers import load_providers

from knowledge.knowledge_ingestion import KnowledgeIngestion

from knowledge.knowledge_query_service import KnowledgeQueryService

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

from model_orchestration.fallback.fallback_manager import FallbackManager

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.registry.model_registry import ModelRegistry

from orchestration.provider_manager import ProviderManager

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

# Memory initialization

load_memory_providers()

MemoryManager.initialize()

# Knowledge ingestion

KnowledgeIngestion.ingest("knowledge/tmforum/tmf641.md")

# Provider initialization

ProviderManager.load()

load_providers()

# Model initialization

ModelRegistry.load()

RoutingPolicy.load()

FallbackManager.load()

# Execute query

result = KnowledgeQueryService.ask("What is Service Order Management")

print(result)
