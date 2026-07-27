from cost_management.usage_tracker import UsageTracker

from cost_management.cost_service import CostService


class CostDashboard:
    @staticmethod
    def generate():

        usage = UsageTracker.get_usage()

        return {service: CostService.calculate(service) for service in usage}
