from self_healing.defect_prevention.defect_prevention_result import (
    DefectPreventionResult,
)


class DefectPreventionService:
    @staticmethod
    def analyze(risk_type):

        recommendations = {
            "api": "add_api_validation_tests",
            "billing": "add_billing_regression_suite",
            "workflow": "add_workflow_retry_validation",
            "ui": "add_ui_regression_suite",
        }

        recommendation = recommendations.get(risk_type, "manual_review")

        result = DefectPreventionResult(
            risk_type=risk_type, recommendation=recommendation, prevented=True
        )

        return result.to_dict()
