from self_healing.test_healing.test_healing_result import TestHealingResult


class TestHealingService:
    @staticmethod
    def heal(test_case):

        result = TestHealingResult(
            test_case=test_case, recovery_action="test_retry", healed=True
        )

        return result.to_dict()
