from execution.base_execution import BaseExecution

from execution.security.owasp_validator import OWASPValidator

from execution.security.security_result import SecurityResult


class SecurityExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        target = test_case.get("target")

        scan = OWASPValidator.scan(target)

        result = SecurityResult(
            status="passed", scan_type="owasp", findings=scan["issues_found"]
        )

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
