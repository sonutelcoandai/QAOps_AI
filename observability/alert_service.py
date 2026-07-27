from observability.alert_manager import AlertManager


class AlertService:
    @staticmethod
    def create_alert(component, message):

        alert = {"component": component, "alert": message}

        AlertManager.add_alert(alert)

        return alert
