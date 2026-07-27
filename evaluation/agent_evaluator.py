from evaluation.scoring_engine import ScoringEngine

from evaluation.agent_report import AgentReport


class AgentEvaluator:
    @staticmethod
    def evaluate(agent_name, agent_result):

        score = 100

        if not agent_result:
            score = 50

        status = ScoringEngine.calculate_score(score)

        report = AgentReport(agent_name, score, status)

        return report.to_dict()
