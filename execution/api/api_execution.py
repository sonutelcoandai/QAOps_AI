from execution.base_execution import BaseExecution

from execution.api.api_client import APIClient

from execution.api.api_result import APIResult

from execution.api.api_validator import APIValidator


class APIExecution(BaseExecution):
    def __init__(self):

        self.results = []

        self.client = APIClient()

    def execute_test(self, test_case):

        response = self.client.execute(
            endpoint=test_case.get("endpoint"),
            method=test_case.get("method", "GET"),
            payload=test_case.get("payload"),
        )

        result = APIResult(status="passed", response_data=response, response_code=200)

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
