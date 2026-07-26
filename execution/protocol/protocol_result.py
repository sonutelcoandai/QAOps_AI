class ProtocolResult:
    def __init__(self, status, protocol, operation):

        self.status = status
        self.protocol = protocol
        self.operation = operation

    def to_dict(self):

        return {
            "status": self.status,
            "protocol": self.protocol,
            "operation": self.operation,
        }
