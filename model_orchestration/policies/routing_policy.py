from config_loader import ConfigLoader


class RoutingPolicy:
    config = {}

    @classmethod
    def load(cls):

        cls.config = ConfigLoader.load_config("llm-routing.yaml")

    @classmethod
    def get_strategy(cls):

        return cls.config.get("routing_strategy", "task_based")

    @classmethod
    def get_tasks(cls):

        return cls.config.get("tasks", {})

    @classmethod
    def get_agents(cls):

        return cls.config.get("agents", {})

    @classmethod
    def get_domains(cls):

        return cls.config.get("domains", {})
