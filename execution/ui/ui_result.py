class UIResult:
    def __init__(self, status, page, locator):

        self.status = status

        self.page = page

        self.locator = locator

    def to_dict(self):

        return {"status": self.status, "page": self.page, "locator": self.locator}
