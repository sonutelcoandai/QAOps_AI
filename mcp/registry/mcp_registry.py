class MCPRegistry:
    servers = {}

    @classmethod
    def register(cls, name, server):

        cls.servers[name] = server

    @classmethod
    def get(cls, name):

        return cls.servers.get(name)

    @classmethod
    def get_all(cls):

        return cls.servers
