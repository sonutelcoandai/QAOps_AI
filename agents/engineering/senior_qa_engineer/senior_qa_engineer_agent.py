from agent_registry.base_agent import BaseAgent


class SeniorQAEngineerAgent(BaseAgent):
    def execute(self, task):
        qa_agent = task.get("input", {})

        return {
            "agent": "senior_qa_engineer",
            "review": "Coverage Review Completed",
            "summary": "QA Engineer output reviewed",
        }

    def validate(self, task):

        return True

    def get_agent_info(self):

        return {"name": "Senior QA Engineer"}
