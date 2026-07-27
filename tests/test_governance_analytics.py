from governance_analytics.governance_service import GovernanceService

from governance_analytics.analytics_service import AnalyticsService

print(GovernanceService.evaluate("telecom_validation"))

print(AnalyticsService.generate("workflow_success_rate", 98))
