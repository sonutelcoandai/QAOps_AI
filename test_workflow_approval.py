from human_in_loop.approval_request import ApprovalRequest

request = ApprovalRequest("REQ-001", "Release Approval", "qa_manager")

print(request.is_approved())  # False

request.approve()

print(request.is_approved())  # True

print(request.to_dict())
