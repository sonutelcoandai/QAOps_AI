from workflows.blueprints.load_blueprints import load_blueprints

from workflows.blueprints.blueprint_registry import BlueprintRegistry

load_blueprints()

print(BlueprintRegistry.get_all())
