from agent_registry.base_agent import BaseAgent

from orchestration.agent_execution_engine import AgentExecutionEngine


class TelecomArchitectAgent(BaseAgent):
    def execute(self, task):

        query = task.get("query", "")

        tmforum_result = AgentExecutionEngine.execute("tmforum_agent", {"query": query})

        billing_result = AgentExecutionEngine.execute("billing_agent", {"query": query})

        oss_result = AgentExecutionEngine.execute("oss_agent", {"query": query})

        bss_result = AgentExecutionEngine.execute("bss_agent", {"query": query})

        return {
            "agent": "telecom_architect_agent",
            "query": query,
            "domain_analysis": {
                "tmforum": tmforum_result,
                "billing": billing_result,
                "oss": oss_result,
                "bss": bss_result,
            },
            "recommendation": "Telecom domain review completed",
        }

    def validate(self, task):

        return "query" in task

    def get_agent_info(self):

        return {"name": "Telecom Architect Agent", "domain": "telecom"}
