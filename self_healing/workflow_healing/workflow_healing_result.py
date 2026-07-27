class WorkflowHealingResult:
    def __init__(self, workflow, recovery_action, healed):

        self.workflow = workflow

        self.recovery_action = recovery_action

        self.healed = healed

    def to_dict(self):

        return {
            "workflow": self.workflow,
            "recovery_action": self.recovery_action,
            "healed": self.healed,
        }
