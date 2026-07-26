from execution.performance.performance_execution import PerformanceExecution

executor = PerformanceExecution()

result = executor.execute_test({"virtual_users": 500})

print(result)

print(executor.collect_results())
