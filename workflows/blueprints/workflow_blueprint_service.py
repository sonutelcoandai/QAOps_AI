from workflows.blueprints.blueprint_registry import BlueprintRegistry

from workflows.blueprints.blueprint_execution_builder import BlueprintExecutionBuilder


class WorkflowBlueprintService:
    @staticmethod
    def get_graph(blueprint_name):

        blueprint = BlueprintRegistry.get(blueprint_name)

        if blueprint is None:
            raise ValueError(f"Blueprint '{blueprint_name}' not found")

        return BlueprintExecutionBuilder.build(blueprint)
