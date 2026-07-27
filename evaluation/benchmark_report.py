class BenchmarkReport:
    def __init__(self, average_score, grade):

        self.average_score = average_score

        self.grade = grade

    def to_dict(self):

        return {"average_score": self.average_score, "grade": self.grade}
