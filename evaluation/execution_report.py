class ExecutionReport:
    def __init__(self, execution_type, score, status):

        self.execution_type = execution_type

        self.score = score

        self.status = status

    def to_dict(self):

        return {
            "execution_type": self.execution_type,
            "score": self.score,
            "status": self.status,
        }
