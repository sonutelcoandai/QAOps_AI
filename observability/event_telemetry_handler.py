from observability.telemetry_service import TelemetryService


class EventTelemetryHandler:
    @staticmethod
    def handle(event):

        TelemetryService.record(event.event_type)
