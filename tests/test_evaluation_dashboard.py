from evaluation.evaluation_dashboard import EvaluationDashboard

result = EvaluationDashboard.generate(
    workflow_score=95, agent_score=90, execution_score=85
)

print(result)
