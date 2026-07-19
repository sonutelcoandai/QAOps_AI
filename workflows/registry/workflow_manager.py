from config_loader import ConfigLoader


class WorkflowManager:
    workflows = {}

    @classmethod
    def load(cls):

        config = ConfigLoader.load_config("workflows.yaml")

        cls.workflows = config["workflows"]

    @classmethod
    def get_workflow_config(cls, workflow_name):

        return cls.workflows.get(workflow_name)

    @classmethod
    def get_all(cls):

        return cls.workflows
