class ScoringEngine:
    @staticmethod
    def calculate_score(score):

        if score >= 90:
            return "excellent"

        if score >= 75:
            return "good"

        if score >= 60:
            return "acceptable"

        return "needs_improvement"
