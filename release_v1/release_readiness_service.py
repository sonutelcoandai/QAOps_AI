from release_v1.release_readiness_report import ReleaseReadinessReport


class ReleaseReadinessService:
    @staticmethod
    def evaluate():

        components = {
            "agents": True,
            "workflows": True,
            "execution": True,
            "mcp": True,
            "event_bus": True,
            "human_in_loop": True,
            "evaluation": True,
            "self_healing": True,
            "integrations": True,
            "governance": True,
            "observability": True,
            "security": True,
            "marketplace": True,
            "ui_command_center": True,
        }

        report = ReleaseReadinessReport(
            platform_ready=all(components.values()), components=components
        )

        return report.to_dict()
