from ai_providers.load_providers import load_providers

from agent_registry.load_agents import load_agents

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

from knowledge.knowledge_pack_loader import KnowledgePackLoader

from orchestration.agent_execution_engine import AgentExecutionEngine

from orchestration.provider_manager import ProviderManager

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.fallback.fallback_manager import FallbackManager

# Memory

load_memory_providers()
MemoryManager.initialize()
KnowledgePackLoader.load_all()

# Providers

ProviderManager.load()
load_providers()

# Models

ModelRegistry.load()
RoutingPolicy.load()
FallbackManager.load()

# Agents

load_agents()

# Execute

result = AgentExecutionEngine.execute(
    "qa_engineer", {"requirement": "Generate TMF641 API test cases"}
)

print(result)
