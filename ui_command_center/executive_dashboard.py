from ui_command_center.command_center_dashboard import CommandCenterDashboard

from ui_command_center.release_readiness_service import ReleaseReadinessService


class ExecutiveDashboard:
    @staticmethod
    def generate():

        return {
            "command_center": CommandCenterDashboard.generate(),
            "release_readiness": ReleaseReadinessService.evaluate(),
        }
