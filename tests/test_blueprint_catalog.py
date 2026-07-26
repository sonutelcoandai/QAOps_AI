from workflows.blueprints.load_blueprints import load_blueprints

from workflows.blueprints.blueprint_catalog import BlueprintCatalog

load_blueprints()

print(BlueprintCatalog.list_blueprints())
