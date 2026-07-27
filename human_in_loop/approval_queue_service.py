from human_in_loop.approval_queue import ApprovalQueue


class ApprovalQueueService:
    @staticmethod
    def get_pending():

        return ApprovalQueue.get_pending()

    @staticmethod
    def get_approved():

        return ApprovalQueue.get_approved()

    @staticmethod
    def get_rejected():

        return ApprovalQueue.get_rejected()

    @staticmethod
    def find_by_id(request_id):

        return ApprovalQueue.find_by_id(request_id)
