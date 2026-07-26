from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

result = AgentExecutionEngine.execute(
    "bss_agent", {"query": "What is BSS customer order management?"}
)

print(result)
