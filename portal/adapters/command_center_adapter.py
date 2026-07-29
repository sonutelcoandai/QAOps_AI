from ui_command_center.executive_dashboard import ExecutiveDashboard


class CommandCenterAdapter:
    @staticmethod
    def get_dashboard():

        return ExecutiveDashboard.generate()
