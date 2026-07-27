from human_in_loop.workflow_approval_service import WorkflowApprovalService

from human_in_loop.approval_service import ApprovalService

from human_in_loop.approval_queue_service import ApprovalQueueService

request_1 = WorkflowApprovalService.request_approval("release_readiness", "qa_manager")

request_2 = WorkflowApprovalService.request_approval("telecom_validation", "qa_lead")

ApprovalService.approve(request_1.request_id)

print("Approved:")

for item in ApprovalQueueService.get_approved():
    print(item.to_dict())

print()

print("Pending:")

for item in ApprovalQueueService.get_pending():
    print(item.to_dict())
