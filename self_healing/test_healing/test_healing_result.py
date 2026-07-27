class TestHealingResult:
    def __init__(self, test_case, recovery_action, healed):

        self.test_case = test_case

        self.recovery_action = recovery_action

        self.healed = healed

    def to_dict(self):

        return {
            "test_case": self.test_case,
            "recovery_action": self.recovery_action,
            "healed": self.healed,
        }
