from agent_registry.base_agent import BaseAgent


class TestArchitectAgent(BaseAgent):
    def execute(self, task):
        return {
            "agent": "test_architect",
            "review": "Architecture Review Completed",
            "summary": "Coverage review approved",
        }

    def validate(self, task):

        return True

    def get_agent_info(self):

        return {"name": "Test Architect"}
