class EvaluationMetrics:
    @staticmethod
    def calculate(workflow_score, agent_score, execution_score):

        average = (workflow_score + agent_score + execution_score) / 3

        return {
            "workflow_score": workflow_score,
            "agent_score": agent_score,
            "execution_score": execution_score,
            "average_score": round(average, 2),
        }
