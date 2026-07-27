class AgentReport:
    def __init__(self, agent, score, status):

        self.agent = agent

        self.score = score

        self.status = status

    def to_dict(self):

        return {"agent": self.agent, "score": self.score, "status": self.status}
