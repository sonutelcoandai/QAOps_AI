from human_in_loop.workflow_approval_service import WorkflowApprovalService


class ApprovalGate:
    @staticmethod
    def create_gate(workflow_name, requester):

        return WorkflowApprovalService.request_approval(workflow_name, requester)

    @staticmethod
    def evaluate(approval_request):

        if approval_request.is_approved():
            return "approved"

        if approval_request.is_rejected():
            return "rejected"

        return "pending"
