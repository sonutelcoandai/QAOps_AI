from human_in_loop.workflow_gate_service import WorkflowGateService

result = WorkflowGateService.require_approval("release_readiness", "qa_manager")

print(result["status"])

print(result["approval_request"].request_id)
