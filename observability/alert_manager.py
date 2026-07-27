class AlertManager:
    alerts = []

    @classmethod
    def add_alert(cls, alert):

        cls.alerts.append(alert)

    @classmethod
    def get_alerts(cls):

        return cls.alerts
