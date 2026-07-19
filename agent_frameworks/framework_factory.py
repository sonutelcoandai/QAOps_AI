from agent_frameworks.framework_registry import FrameworkRegistry


class FrameworkFactory:
    @staticmethod
    def get_framework(framework_name):

        framework = FrameworkRegistry.get(framework_name)

        if framework is None:
            raise ValueError(f"Framework '{framework_name}' not found")

        return framework
