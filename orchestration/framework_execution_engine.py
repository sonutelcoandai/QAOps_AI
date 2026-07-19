from agent_frameworks.framework_factory import FrameworkFactory

from orchestration.framework_manager import FrameworkManager


class FrameworkExecutionEngine:
    @staticmethod
    def execute(workflow_function):

        framework_name = FrameworkManager.get_default_framework()

        framework = FrameworkFactory.get_framework(framework_name)

        return framework.execute(workflow_function)
