from human_in_loop.approval_queue import ApprovalQueue

from human_in_loop.approval_request import ApprovalRequest


class ApprovalService:
    @staticmethod
    def create_request(request_id, title, requester):

        request = ApprovalRequest(request_id, title, requester)

        ApprovalQueue.add(request)

        return request

    @staticmethod
    def approve(request_id):

        for request in ApprovalQueue.get_all():
            if request.request_id == request_id:
                request.approve()

                return request

        return None

    @staticmethod
    def reject(request_id):

        for request in ApprovalQueue.get_all():
            if request.request_id == request_id:
                request.reject()

                return request

        return None
