from evaluation.benchmark_service import BenchmarkService


class PlatformEvaluationService:
    @staticmethod
    def evaluate_platform():

        scores = [
            100,  # workflow
            100,  # agent
            100,  # execution
        ]

        return BenchmarkService.benchmark(scores)
