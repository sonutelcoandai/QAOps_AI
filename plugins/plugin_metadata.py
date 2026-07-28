class PluginMetadata:
    def __init__(self, name, version, status):

        self.name = name
        self.version = version
        self.status = status

    def to_dict(self):

        return {"name": self.name, "version": self.version, "status": self.status}
