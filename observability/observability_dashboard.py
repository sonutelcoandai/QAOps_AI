from observability.health_monitor import HealthMonitor

from observability.telemetry_service import TelemetryService

from observability.alert_manager import AlertManager


class ObservabilityDashboard:
    @staticmethod
    def generate():

        return {
            "health": {
                "workflow_engine": HealthMonitor.check("workflow_engine"),
                "agent_engine": HealthMonitor.check("agent_engine"),
                "mcp": HealthMonitor.check("mcp"),
            },
            "telemetry": TelemetryService.get_metrics(),
            "alerts": AlertManager.get_alerts(),
        }
