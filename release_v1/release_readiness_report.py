class ReleaseReadinessReport:
    def __init__(self, platform_ready, components):

        self.platform_ready = platform_ready
        self.components = components

    def to_dict(self):

        return {"platform_ready": self.platform_ready, "components": self.components}
