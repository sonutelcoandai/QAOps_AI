class EvaluationResult:
    def __init__(self, score, status):

        self.score = score

        self.status = status

    def to_dict(self):

        return {"score": self.score, "status": self.status}
