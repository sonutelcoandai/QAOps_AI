from workflows.registry.workflow_catalog import WorkflowCatalog


class WorkflowCommandCenter:
    @staticmethod
    def generate():

        try:
            workflows = WorkflowCatalog.get_all()

        except Exception:
            workflows = {}

        return {"workflows": workflows}
