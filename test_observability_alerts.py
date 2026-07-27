from observability.alert_service import AlertService

from observability.observability_dashboard import ObservabilityDashboard

AlertService.create_alert("workflow_engine", "High workflow failure rate")

print(ObservabilityDashboard.generate())
