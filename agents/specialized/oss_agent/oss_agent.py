from agent_registry.base_agent import BaseAgent

from knowledge.knowledge_query_service import KnowledgeQueryService


class OSSAgent(BaseAgent):
    def execute(self, task):

        query = task.get("query", "")

        response = KnowledgeQueryService.ask(query)

        return {"agent": "oss_agent", "query": query, "response": response}

    def validate(self, task):

        return "query" in task

    def get_agent_info(self):

        return {"name": "OSS Agent", "domain": "oss"}
