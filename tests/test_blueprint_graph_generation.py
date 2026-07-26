from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.blueprints.load_blueprints import load_blueprints

from workflows.blueprints.workflow_blueprint_service import WorkflowBlueprintService

PlatformBootstrap.initialize()

load_blueprints()

graph = WorkflowBlueprintService.get_graph("requirement_to_test")

result = graph.execute({"requirement": "Generate TMF641 API test cases"})

print(result.keys())
