from evaluation.evaluation_result import EvaluationResult

from evaluation.scoring_engine import ScoringEngine


class EvaluationService:
    @staticmethod
    def evaluate(score):

        status = ScoringEngine.calculate_score(score)

        result = EvaluationResult(score, status)

        return result.to_dict()
