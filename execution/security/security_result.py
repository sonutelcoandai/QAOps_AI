class SecurityResult:
    def __init__(self, status, scan_type, findings):

        self.status = status
        self.scan_type = scan_type
        self.findings = findings

    def to_dict(self):

        return {
            "status": self.status,
            "scan_type": self.scan_type,
            "findings": self.findings,
        }
