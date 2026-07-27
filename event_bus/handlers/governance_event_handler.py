class GovernanceEventHandler:
    @staticmethod
    def handle(event):

        print(f"[Governance] {event.event_type}")
