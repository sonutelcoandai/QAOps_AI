from governance_analytics.analytics_report import AnalyticsReport


class AnalyticsService:
    @staticmethod
    def generate(metric, value):

        report = AnalyticsReport(metric, value)

        return report.to_dict()
