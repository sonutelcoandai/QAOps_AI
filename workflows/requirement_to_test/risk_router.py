class RiskRouter:
    @staticmethod
    def evaluate(payload):

        requirement = payload.get("requirement", "").lower()

        high_risk_keywords = [
            "billing",
            "charging",
            "payment",
            "production",
            "security",
        ]

        for keyword in high_risk_keywords:
            if keyword in requirement:
                return "high"

        return "normal"
