class SecurityAuditReport:
    def __init__(self, target, result):

        self.target = target

        self.result = result

    def to_dict(self):

        return {"target": self.target, "result": self.result}
