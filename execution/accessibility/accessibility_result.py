class AccessibilityResult:
    def __init__(self, status, violations):

        self.status = status
        self.violations = violations

    def to_dict(self):

        return {"status": self.status, "violations": self.violations}
