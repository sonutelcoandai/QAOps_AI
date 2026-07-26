from execution.protocol.protocol_execution import ProtocolExecution

executor = ProtocolExecution()

print(executor.execute_test({"protocol": "sip", "operation": "invite"}))

print(executor.execute_test({"protocol": "diameter", "operation": "credit-control"}))

print(executor.collect_results())
