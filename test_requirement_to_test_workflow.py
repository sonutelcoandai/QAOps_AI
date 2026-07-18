from ai_providers.load_providers import load_providers

from agent_registry.load_agents import load_agents

from knowledge.knowledge_pack_loader import KnowledgePackLoader

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers

from model_orchestration.fallback.fallback_manager import FallbackManager

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.registry.model_registry import ModelRegistry

from orchestration.provider_manager import ProviderManager

from workflows.requirement_to_test.requirement_to_test_workflow import (
    RequirementToTestWorkflow,
)

load_memory_providers()
MemoryManager.initialize()
KnowledgePackLoader.load_all()

ProviderManager.load()
load_providers()

ModelRegistry.load()
RoutingPolicy.load()
FallbackManager.load()

load_agents()

result = RequirementToTestWorkflow.execute("Generate TMF641 API Test Cases")

print(result)
