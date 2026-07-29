class ArchitectureValidationReport:
    def __init__(self, valid, components):

        self.valid = valid
        self.components = components

    def to_dict(self):

        return {"architecture_valid": self.valid, "components": self.components}
