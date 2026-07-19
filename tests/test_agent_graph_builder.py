from orchestration.platform_bootstrap import PlatformBootstrap

from agent_frameworks.langgraph.agent_graph_builder import AgentGraphBuilder

PlatformBootstrap.initialize()

graph = AgentGraphBuilder.build(["qa_engineer"])

result = graph.execute({"requirement": "Generate TMF641 API test cases"})

print(result)
