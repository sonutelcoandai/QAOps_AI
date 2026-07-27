from evaluation.benchmark_report import BenchmarkReport


class BenchmarkService:
    @staticmethod
    def benchmark(scores):

        if not scores:
            average_score = 0

        else:
            average_score = sum(scores) / len(scores)

        if average_score >= 90:
            grade = "A"

        elif average_score >= 75:
            grade = "B"

        elif average_score >= 60:
            grade = "C"

        else:
            grade = "D"

        report = BenchmarkReport(round(average_score, 2), grade)

        return report.to_dict()
