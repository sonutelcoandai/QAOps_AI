from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

result = AgentExecutionEngine.execute(
    "telecom_architect_agent", {"query": "Validate TMF641 billing integration"}
)

print(result)
