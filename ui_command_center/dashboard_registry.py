class DashboardRegistry:
    dashboards = {}

    @classmethod
    def register(cls, name, dashboard):

        cls.dashboards[name] = dashboard

    @classmethod
    def get_all(cls):

        return cls.dashboards
