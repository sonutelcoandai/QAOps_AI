from agent_registry.agent_factory import AgentFactory


class AgentExecutionEngine:
    @staticmethod
    def execute(agent_name, task):

        agent = AgentFactory.get_agent(agent_name)

        return agent.execute(task)
