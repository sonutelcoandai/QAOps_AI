from execution.base_execution import BaseExecution

from execution.contract.contract_result import ContractResult

from execution.contract.openapi_validator import OpenAPIValidator

from execution.contract.schema_validator import SchemaValidator


class ContractExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        contract_name = test_case.get("contract")

        payload = test_case.get("payload", {})

        contract_result = OpenAPIValidator.validate_contract(contract_name)

        schema_result = SchemaValidator.validate(payload, contract_name)

        result = ContractResult(
            status="passed", schema=contract_name, validation=schema_result
        )

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
