class MobileResult:
    def __init__(self, status, platform, screen):

        self.status = status
        self.platform = platform
        self.screen = screen

    def to_dict(self):

        return {"status": self.status, "platform": self.platform, "screen": self.screen}
