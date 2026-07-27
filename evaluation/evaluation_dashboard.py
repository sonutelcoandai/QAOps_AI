from evaluation.evaluation_metrics import EvaluationMetrics

from evaluation.benchmark_service import BenchmarkService


class EvaluationDashboard:
    @staticmethod
    def generate(workflow_score, agent_score, execution_score):

        metrics = EvaluationMetrics.calculate(
            workflow_score, agent_score, execution_score
        )

        benchmark = BenchmarkService.benchmark(
            [workflow_score, agent_score, execution_score]
        )

        return {"metrics": metrics, "benchmark": benchmark}
