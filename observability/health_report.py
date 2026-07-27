class HealthReport:
    def __init__(self, component, status):

        self.component = component

        self.status = status

    def to_dict(self):

        return {"component": self.component, "status": self.status}
