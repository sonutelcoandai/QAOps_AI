class ApprovalRequest:
    def __init__(self, request_id, title, requester):

        self.request_id = request_id

        self.title = title

        self.requester = requester

        self.status = "pending"

    def approve(self):

        self.status = "approved"

    def reject(self):

        self.status = "rejected"

    def is_approved(self):

        return self.status == "approved"

    def is_rejected(self):

        return self.status == "rejected"

    def to_dict(self):

        return {
            "request_id": self.request_id,
            "title": self.title,
            "requester": self.requester,
            "status": self.status,
        }
