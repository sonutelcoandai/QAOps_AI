from human_in_loop.workflow_approval_service import WorkflowApprovalService

from human_in_loop.approval_decision_service import ApprovalDecisionService

request = WorkflowApprovalService.request_approval("release_readiness", "qa_manager")

print(request.status)

ApprovalDecisionService.approve(request.request_id)

print(request.status)
