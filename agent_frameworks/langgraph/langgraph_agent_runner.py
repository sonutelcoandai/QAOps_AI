from orchestration.agent_execution_engine import AgentExecutionEngine


class LangGraphAgentRunner:
    @staticmethod
    def execute_agent(agent_name, task):

        return AgentExecutionEngine.execute(agent_name, task)
