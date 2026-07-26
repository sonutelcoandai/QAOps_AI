from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

result = AgentExecutionEngine.execute(
    "billing_agent", {"query": "How do I validate telecom billing?"}
)

print(result)
