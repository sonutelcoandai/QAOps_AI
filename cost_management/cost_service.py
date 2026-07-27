from cost_management.cost_report import CostReport

from cost_management.usage_tracker import UsageTracker


class CostService:
    COST_PER_EXECUTION = 0.01

    @classmethod
    def calculate(cls, service_name):

        usage = UsageTracker.get_usage().get(service_name, 0)

        cost = usage * cls.COST_PER_EXECUTION

        report = CostReport(service=service_name, cost=round(cost, 2))

        return report.to_dict()
