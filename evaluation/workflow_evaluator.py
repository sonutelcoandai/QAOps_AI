from evaluation.scoring_engine import ScoringEngine

from evaluation.workflow_report import WorkflowReport


class WorkflowEvaluator:
    @staticmethod
    def evaluate(workflow_name, workflow_result):

        score = 100

        if workflow_result.get("status") != "completed":
            score = 50

        status = ScoringEngine.calculate_score(score)

        report = WorkflowReport(workflow_name, score, status)

        return report.to_dict()
