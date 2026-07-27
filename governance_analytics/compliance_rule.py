class ComplianceRule:
    RULES = {
        "telecom_validation": "compliant",
        "billing_validation": "compliant",
        "release_readiness": "approval_required",
    }

    @classmethod
    def get_rule(cls, item):

        return cls.RULES.get(item, "review_required")
