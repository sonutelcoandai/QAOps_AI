class WorkflowRegistry:
    workflows = {}

    @classmethod
    def register(cls, workflow_name, workflow_instance):

        cls.workflows[workflow_name] = workflow_instance

    @classmethod
    def get(cls, workflow_name):

        return cls.workflows.get(workflow_name)

    @classmethod
    def get_all(cls):

        return cls.workflows
