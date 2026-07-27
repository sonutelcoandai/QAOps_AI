from evaluation.workflow_evaluator import WorkflowEvaluator

result = WorkflowEvaluator.evaluate("telecom_validation", {"status": "completed"})

print(result)
