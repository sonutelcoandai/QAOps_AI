class GovernancePolicy:
    POLICIES = {
        "telecom_validation": "approved",
        "billing_validation": "approved",
        "requirement_to_test": "approved",
    }

    @classmethod
    def get_policy(cls, workflow_name):

        return cls.POLICIES.get(workflow_name, "review_required")
