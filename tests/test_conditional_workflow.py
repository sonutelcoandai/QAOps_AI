from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.requirement_to_test.workflow_graph_builder import WorkflowGraphBuilder

PlatformBootstrap.initialize()

graph = WorkflowGraphBuilder.build()

result = graph.execute({"requirement": "Generate billing system test cases"})

print(result["architect_result"])
