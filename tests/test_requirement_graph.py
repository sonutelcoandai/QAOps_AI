from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.requirement_to_test.workflow_graph_builder import WorkflowGraphBuilder

PlatformBootstrap.initialize()

graph = WorkflowGraphBuilder.build()

result = graph.execute({"requirement": "Generate TMF641 API test cases"})

print(result.keys())
