from evaluation.scoring_engine import ScoringEngine

from evaluation.execution_report import ExecutionReport


class ExecutionEvaluator:
    @staticmethod
    def evaluate(execution_type, execution_result):

        score = 100

        if execution_result.get("status") not in ["passed", "completed"]:
            score = 50

        status = ScoringEngine.calculate_score(score)

        report = ExecutionReport(execution_type, score, status)

        return report.to_dict()
