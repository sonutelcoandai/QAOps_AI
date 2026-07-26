from execution.base_execution import BaseExecution

from execution.protocol.sip_execution import SIPExecution

from execution.protocol.diameter_execution import DiameterExecution

from execution.protocol.smpp_execution import SMPPExecution


class ProtocolExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        protocol = test_case.get("protocol")

        operation = test_case.get("operation")

        if protocol == "sip":
            result = SIPExecution.execute(operation)

        elif protocol == "diameter":
            result = DiameterExecution.execute(operation)

        elif protocol == "smpp":
            result = SMPPExecution.execute(operation)

        else:
            raise ValueError(f"Unsupported protocol: {protocol}")

        self.results.append(result)

        return result

    def collect_results(self):

        return self.results
