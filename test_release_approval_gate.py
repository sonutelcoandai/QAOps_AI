from human_in_loop.release_approval_gate import ReleaseApprovalGate

from human_in_loop.approval_service import ApprovalService

request = ReleaseApprovalGate.request("qa_manager")

print(request.status)

print(ReleaseApprovalGate.can_proceed(request))

ApprovalService.approve(request.request_id)

print(request.status)

print(ReleaseApprovalGate.can_proceed(request))
