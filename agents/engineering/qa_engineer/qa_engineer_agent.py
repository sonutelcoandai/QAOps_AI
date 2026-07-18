from agent_registry.base_agent import BaseAgent

from knowledge.knowledge_query_service import KnowledgeQueryService


class QAEngineerAgent(BaseAgent):
    def execute(self, task):

        requirement = task["requirement"]

        response = KnowledgeQueryService.ask(requirement)

        return {"agent": "qa_engineer", "result": response}

    def validate(self, task):

        return "requirement" in task

    def get_agent_info(self):

        return {"name": "QA Engineer Agent"}
