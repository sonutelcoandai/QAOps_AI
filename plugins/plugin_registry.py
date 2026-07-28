class PluginRegistry:
    plugins = {}

    @classmethod
    def register(cls, name, plugin):

        cls.plugins[name] = plugin

    @classmethod
    def get(cls, name):

        return cls.plugins.get(name)

    @classmethod
    def get_all(cls):

        return cls.plugins
