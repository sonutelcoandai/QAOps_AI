class BlueprintRegistry:
    blueprints = {}

    @classmethod
    def register(cls, blueprint_name, blueprint):

        cls.blueprints[blueprint_name] = blueprint

    @classmethod
    def get(cls, blueprint_name):

        return cls.blueprints.get(blueprint_name)

    @classmethod
    def get_all(cls):

        return cls.blueprints
