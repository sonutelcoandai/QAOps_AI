from observability.telemetry_service import TelemetryService

from observability.observability_dashboard import ObservabilityDashboard

TelemetryService.record("workflow_engine")

TelemetryService.record("workflow_engine")

print(ObservabilityDashboard.generate())
