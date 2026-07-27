class ComplianceReport:
    def __init__(self, item, result):

        self.item = item

        self.result = result

    def to_dict(self):

        return {"item": self.item, "result": self.result}
