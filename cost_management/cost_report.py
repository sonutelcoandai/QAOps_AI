class CostReport:
    def __init__(self, service, cost):

        self.service = service

        self.cost = cost

    def to_dict(self):

        return {"service": self.service, "cost": self.cost}
