from execution.base_execution import BaseExecution

from execution.performance.load_test import LoadTest

from execution.performance.performance_result import PerformanceResult


class PerformanceExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        load_result = LoadTest.run(test_case.get("virtual_users", 100))

        result = PerformanceResult(
            status="passed",
            virtual_users=load_result["virtual_users"],
            response_time=load_result["average_response_time"],
        )

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
