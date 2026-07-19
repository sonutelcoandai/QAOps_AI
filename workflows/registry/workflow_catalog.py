from workflows.registry.workflow_manager import WorkflowManager


class WorkflowCatalog:
    @staticmethod
    def list_workflows():

        return list(WorkflowManager.get_all().keys())

    @staticmethod
    def get_active_workflows():

        active = []

        for workflow_name, config in WorkflowManager.get_all().items():
            if config.get("status") == "active":
                active.append(workflow_name)

        return active

    @staticmethod
    def get_workflow_info(workflow_name):

        return WorkflowManager.get_workflow_config(workflow_name)

    @staticmethod
    def get_workflows_by_category(category):

        workflows = []

        for workflow_name, config in WorkflowManager.get_all().items():
            if config.get("category") == category:
                workflows.append(workflow_name)

        return workflows

    @staticmethod
    def get_workflows_by_domain(domain):

        workflows = []

        for workflow_name, config in WorkflowManager.get_all().items():
            domains = config.get("supported_domains", [])

            if domain in domains:
                workflows.append(workflow_name)

        return workflows

    @staticmethod
    def list_workflow_details():

        details = {}

        for workflow_name, config in WorkflowManager.get_all().items():
            details[workflow_name] = {
                "version": config.get("version"),
                "status": config.get("status"),
                "category": config.get("category"),
            }

        return details
