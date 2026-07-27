class DefectPreventionResult:
    def __init__(self, risk_type, recommendation, prevented):

        self.risk_type = risk_type

        self.recommendation = recommendation

        self.prevented = prevented

    def to_dict(self):

        return {
            "risk_type": self.risk_type,
            "recommendation": self.recommendation,
            "prevented": self.prevented,
        }
