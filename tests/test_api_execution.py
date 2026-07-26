from execution.api.api_execution import APIExecution

executor = APIExecution()

result = executor.execute_test(
    {
        "endpoint": "/tmf641/serviceOrder",
        "method": "POST",
        "payload": {"serviceOrder": "123"},
    }
)

print(result)

print(executor.collect_results())
