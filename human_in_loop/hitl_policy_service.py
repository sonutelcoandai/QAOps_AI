class HITLPolicyService:
    APPROVAL_WORKFLOWS = ["release_readiness", "telecom_validation"]

    @classmethod
    def requires_approval(cls, workflow_name):

        return workflow_name in cls.APPROVAL_WORKFLOWS
