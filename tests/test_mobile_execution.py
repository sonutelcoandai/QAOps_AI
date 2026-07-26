from execution.mobile.mobile_execution import MobileExecution

executor = MobileExecution()

result = executor.execute_test({"platform": "android", "screen": "login_screen"})

print(result)

print(executor.collect_results())
