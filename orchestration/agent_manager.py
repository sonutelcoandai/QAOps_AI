from config_loader import ConfigLoader


class AgentManager:
    config = {}

    @classmethod
    def load(cls):

        data = ConfigLoader.load_config("agents.yaml")

        cls.config = data["agents"]

    @classmethod
    def get_agent_config(cls, agent_name):

        return cls.config.get(agent_name)
