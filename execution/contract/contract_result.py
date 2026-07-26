class ContractResult:
    def __init__(self, status, schema, validation):

        self.status = status
        self.schema = schema
        self.validation = validation

    def to_dict(self):

        return {
            "status": self.status,
            "schema": self.schema,
            "validation": self.validation,
        }
