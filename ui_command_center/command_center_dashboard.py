from ui_command_center.dashboard_registry import DashboardRegistry

from ui_command_center.dashboard_metadata import DashboardMetadata

from ui_command_center.operations_command_center import OperationsCommandCenter
from ui_command_center.governance_command_center import GovernanceCommandCenter

from ui_command_center.security_command_center import SecurityCommandCenter
from ui_command_center.integrations_command_center import IntegrationsCommandCenter

from ui_command_center.marketplace_command_center import MarketplaceCommandCenter
from ui_command_center.workflow_command_center import WorkflowCommandCenter

from ui_command_center.agent_command_center import AgentCommandCenter


class CommandCenterDashboard:
    @staticmethod
    def register_default_dashboards():

        DashboardRegistry.register(
            "operations", DashboardMetadata("operations", "operations")
        )

        DashboardRegistry.register(
            "governance", DashboardMetadata("governance", "governance")
        )

        DashboardRegistry.register(
            "security", DashboardMetadata("security", "security")
        )

        DashboardRegistry.register(
            "marketplace", DashboardMetadata("marketplace", "marketplace")
        )

    @staticmethod
    def get_dashboards():

        return {
            name: dashboard.to_dict()
            for name, dashboard in DashboardRegistry.get_all().items()
        }

    @staticmethod
    def generate():

        return {
            "operations": OperationsCommandCenter.generate(),
            "governance": GovernanceCommandCenter.generate(),
            "security": SecurityCommandCenter.generate(),
            "integrations": IntegrationsCommandCenter.generate(),
            "marketplace": MarketplaceCommandCenter.generate(),
            "workflows": WorkflowCommandCenter.generate(),
            "agents": AgentCommandCenter.generate(),
        }
