class AnalyticsReport:
    def __init__(self, metric, value):

        self.metric = metric

        self.value = value

    def to_dict(self):

        return {"metric": self.metric, "value": self.value}
