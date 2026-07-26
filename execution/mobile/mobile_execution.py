from execution.base_execution import BaseExecution

from execution.mobile.mobile_result import MobileResult

from execution.mobile.mobile_validator import MobileValidator


class MobileExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        platform = test_case.get("platform")

        screen = test_case.get("screen")

        MobileValidator.validate_screen(screen)

        result = MobileResult(status="passed", platform=platform, screen=screen)

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
