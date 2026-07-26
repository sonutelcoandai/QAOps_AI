from execution.base_execution import BaseExecution

from execution.accessibility.wcag_validator import WCAGValidator

from execution.accessibility.accessibility_result import AccessibilityResult


class AccessibilityExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        result = WCAGValidator.validate(test_case.get("page"))

        response = AccessibilityResult(status="passed", violations=result["violations"])

        self.results.append(response)

        return response.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
