from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

result = AgentExecutionEngine.execute(
    "oss_agent", {"query": "What is telecom service provisioning?"}
)

print(result)
