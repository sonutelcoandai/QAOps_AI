from human_in_loop.workflow_approval_service import WorkflowApprovalService


class ReleaseApprovalGate:
    @staticmethod
    def request(requester):

        return WorkflowApprovalService.request_approval("release_readiness", requester)

    @staticmethod
    def can_proceed(approval_request):

        return approval_request.is_approved()
