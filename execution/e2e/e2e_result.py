class E2EResult:
    def __init__(self, status, journey):

        self.status = status
        self.journey = journey

    def to_dict(self):

        return {"status": self.status, "journey": self.journey}
