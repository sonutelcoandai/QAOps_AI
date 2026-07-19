from agent_frameworks.framework_factory import FrameworkFactory

from orchestration.framework_manager import FrameworkManager


class AgentCollaboration:
    @staticmethod
    def execute_workflow(task):

        framework_name = FrameworkManager.get_default_framework()

        framework = FrameworkFactory.get_framework(framework_name)

        results = []

        qa_result = framework.execute_agent("qa_engineer", task)

        results.append(qa_result)

        senior_result = framework.execute_agent(
            "senior_qa_engineer", {"agent": qa_result["agent"]}
        )

        results.append(senior_result)

        architect_result = framework.execute_agent(
            "test_architect", {"agent": senior_result["agent"]}
        )

        results.append(architect_result)

        return results
