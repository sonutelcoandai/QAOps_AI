from execution.ui.ui_execution import UIExecution

executor = UIExecution()

result = executor.execute_test({"page": "Login", "locator": "#username"})

print(result)

print(executor.collect_results())
