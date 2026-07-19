from workflows.blueprints.blueprint_registry import BlueprintRegistry


class BlueprintCatalog:
    @staticmethod
    def list_blueprints():

        return list(BlueprintRegistry.get_all().keys())
