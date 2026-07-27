from human_in_loop.approval_queue_service import ApprovalQueueService


class ApprovalMetricsService:
    @staticmethod
    def get_summary():

        return {
            "pending": len(ApprovalQueueService.get_pending()),
            "approved": len(ApprovalQueueService.get_approved()),
            "rejected": len(ApprovalQueueService.get_rejected()),
        }
