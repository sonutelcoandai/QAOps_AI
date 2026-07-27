from human_in_loop.approval_service import ApprovalService

from human_in_loop.approval_queue import ApprovalQueue

ApprovalService.create_request("REQ-001", "Release Approval", "qa_manager")

for request in ApprovalQueue.get_all():
    print(request.request_id, request.title, request.status)
