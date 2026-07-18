from config_loader import ConfigLoader


class ModelRouter:
    routing_rules = {}

    fallback = {}

    @classmethod
    def load(cls):

        config = ConfigLoader.load_config("llm-routing.yaml")

        cls.routing_rules = config["tasks"]

        cls.fallback = config["fallback"]

    @classmethod
    def get_model_for_task(cls, task_name):

        task_config = cls.routing_rules.get(task_name)

        if task_config:
            return task_config["model"]

        return cls.fallback["model"]
