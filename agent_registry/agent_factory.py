from agent_registry.agent_registry import AgentRegistry


class AgentFactory:
    @staticmethod
    def get_agent(agent_name):

        agent = AgentRegistry.get(agent_name)

        if agent is None:
            raise ValueError(f"Agent '{agent_name}' not found")

        return agent
