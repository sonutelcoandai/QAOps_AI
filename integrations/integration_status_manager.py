class IntegrationStatusManager:
    VALID_STATUSES = ["active", "inactive", "deprecated", "retired"]

    statuses = {}

    @classmethod
    def set_status(cls, integration_name, status):

        if status not in cls.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'")

        cls.statuses[integration_name] = status

    @classmethod
    def get_status(cls, integration_name):

        return cls.statuses.get(integration_name, "active")
