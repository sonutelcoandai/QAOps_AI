class ReleaseReport:
    def __init__(self, metadata, certification):

        self.metadata = metadata

        self.certification = certification

    def to_dict(self):

        return {"metadata": self.metadata, "certification": self.certification}
