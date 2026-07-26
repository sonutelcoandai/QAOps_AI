from execution.contract.contract_execution import ContractExecution

executor = ContractExecution()

result = executor.execute_test(
    {"contract": "TMF641", "payload": {"serviceOrder": "123"}}
)

print(result)

print(executor.collect_results())
