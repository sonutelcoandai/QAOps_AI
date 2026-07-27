from governance_analytics.governance_policy import GovernancePolicy


class GovernanceService:
    @staticmethod
    def evaluate(workflow_name):

        return {
            "workflow": workflow_name,
            "policy": GovernancePolicy.get_policy(workflow_name),
        }
