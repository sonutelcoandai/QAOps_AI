from security.security_event_handler import SecurityEventHandler


class SecurityMonitoringService:
    @staticmethod
    def get_summary():

        events = SecurityEventHandler.get_events()

        return {"total_events": len(events), "events": events}
