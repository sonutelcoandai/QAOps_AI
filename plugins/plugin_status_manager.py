class PluginStatusManager:
    VALID_STATUSES = ["active", "inactive", "deprecated", "retired"]

    statuses = {}

    @classmethod
    def set_status(cls, plugin_name, status):

        if status not in cls.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'")

        cls.statuses[plugin_name] = status

    @classmethod
    def get_status(cls, plugin_name):

        return cls.statuses.get(plugin_name, "active")
