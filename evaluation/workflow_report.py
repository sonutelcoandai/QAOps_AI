class WorkflowReport:
    def __init__(self, workflow, score, status):

        self.workflow = workflow
        self.score = score
        self.status = status

    def to_dict(self):

        return {"workflow": self.workflow, "score": self.score, "status": self.status}
