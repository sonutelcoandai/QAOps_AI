from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

result = AgentExecutionEngine.execute("tmforum_agent", {"query": "What is TMF641?"})

print(result)
