import test_agent_events

from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_execution_engine import AgentExecutionEngine

PlatformBootstrap.initialize()

AgentExecutionEngine.execute("tmforum_agent", {"query": "What is TMF641?"})
