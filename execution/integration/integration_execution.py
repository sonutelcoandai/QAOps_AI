from execution.base_execution import BaseExecution

from execution.integration.integration_result import IntegrationResult


class IntegrationExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        result = IntegrationResult(
            status="passed", systems=test_case.get("systems", [])
        )

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
