class SecurityReport:
    def __init__(self, operation, decision):

        self.operation = operation

        self.decision = decision

    def to_dict(self):

        return {"operation": self.operation, "decision": self.decision}
