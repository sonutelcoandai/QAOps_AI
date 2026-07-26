from orchestration.agent_execution_engine import AgentExecutionEngine

from orchestration.telecom_domain_router import TelecomDomainRouter


class TelecomQueryService:
    @staticmethod
    def execute(query):

        agent_name = TelecomDomainRouter.get_agent(query)

        return AgentExecutionEngine.execute(agent_name, {"query": query})
