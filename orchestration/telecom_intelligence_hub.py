from orchestration.telecom_query_service import TelecomQueryService

from orchestration.agent_execution_engine import AgentExecutionEngine


class TelecomIntelligenceHub:
    @staticmethod
    def ask(query):

        specialist_result = TelecomQueryService.execute(query)

        architect_result = AgentExecutionEngine.execute(
            "telecom_architect_agent", {"query": query}
        )

        return {
            "query": query,
            "specialist_analysis": specialist_result,
            "architect_review": architect_result,
            "status": "completed",
        }
