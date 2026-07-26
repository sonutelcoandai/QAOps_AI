from execution.accessibility.accessibility_execution import AccessibilityExecution

executor = AccessibilityExecution()

print(executor.execute_test({"page": "login_page"}))

print(executor.collect_results())
