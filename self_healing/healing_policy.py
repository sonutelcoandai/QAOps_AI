class HealingPolicy:
    POLICIES = {
        "locator": "locator_healing",
        "api": "api_healing",
        "workflow": "workflow_healing",
        "test": "test_healing",
        "defect": "defect_prevention",
        "optimization": "self_optimization",
        "knowledge": "knowledge_evolution",
        "learning": "continuous_learning",
    }

    @classmethod
    def get_action(cls, failure_type):

        return cls.POLICIES.get(failure_type, "manual_intervention")
