class FrameworkRegistry:
    frameworks = {}

    @classmethod
    def register(cls, framework_name, framework_instance):

        cls.frameworks[framework_name] = framework_instance

    @classmethod
    def get(cls, framework_name):

        return cls.frameworks.get(framework_name)

    @classmethod
    def get_all(cls):

        return cls.frameworks
