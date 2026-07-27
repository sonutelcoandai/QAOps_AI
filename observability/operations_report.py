class OperationsReport:
    def __init__(self, dashboard):

        self.dashboard = dashboard

    def to_dict(self):

        return {"operations": self.dashboard}
