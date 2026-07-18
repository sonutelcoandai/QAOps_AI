class AgentRegistry:
    agents = {}

    @classmethod
    def register(cls, agent_name, agent_instance):

        cls.agents[agent_name] = agent_instance

    @classmethod
    def get(cls, agent_name):

        return cls.agents.get(agent_name)

    @classmethod
    def get_all(cls):

        return cls.agents
