class SecurityPolicy:
    POLICIES = {
        "workflow_execution": "allowed",
        "agent_execution": "allowed",
        "integration_execution": "allowed",
        "production_deployment": "approval_required",
    }

    @classmethod
    def get_policy(cls, operation):

        return cls.POLICIES.get(operation, "review_required")
