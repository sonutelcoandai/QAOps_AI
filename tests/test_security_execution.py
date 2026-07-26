from execution.security.security_execution import SecurityExecution

executor = SecurityExecution()

result = executor.execute_test({"target": "/tmf641/serviceOrder"})

print(result)

print(executor.collect_results())
