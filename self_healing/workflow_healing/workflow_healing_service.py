from self_healing.workflow_healing.workflow_healing_result import WorkflowHealingResult


class WorkflowHealingService:
    @staticmethod
    def heal(workflow_name):

        result = WorkflowHealingResult(
            workflow=workflow_name, recovery_action="workflow_restart", healed=True
        )

        return result.to_dict()
