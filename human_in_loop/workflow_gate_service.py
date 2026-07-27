from human_in_loop.approval_gate import ApprovalGate


class WorkflowGateService:
    @staticmethod
    def require_approval(workflow_name, requester):

        request = ApprovalGate.create_gate(workflow_name, requester)

        return {
            "workflow": workflow_name,
            "approval_request": request,
            "status": ApprovalGate.evaluate(request),
        }
