class GovernanceReport:
    def __init__(self, governance, compliance, analytics):

        self.governance = governance

        self.compliance = compliance

        self.analytics = analytics

    def to_dict(self):

        return {
            "governance": self.governance,
            "compliance": self.compliance,
            "analytics": self.analytics,
        }
