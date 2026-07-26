from execution.base_execution import BaseExecution

from execution.e2e.e2e_result import E2EResult


class E2EExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        result = E2EResult(status="passed", journey=test_case.get("journey"))

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
