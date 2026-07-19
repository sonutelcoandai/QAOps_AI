from workflows.blueprints.load_blueprints import load_blueprints

from workflows.blueprints.blueprint_registry import BlueprintRegistry

load_blueprints()

blueprint = BlueprintRegistry.get("requirement_to_test")

print(blueprint.name)

print(blueprint.agents)
