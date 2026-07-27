class TelemetryService:
    telemetry = {}

    @classmethod
    def record(cls, component):

        cls.telemetry[component] = cls.telemetry.get(component, 0) + 1

    @classmethod
    def get_metrics(cls):

        return cls.telemetry
