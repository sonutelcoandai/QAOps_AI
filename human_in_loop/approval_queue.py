class ApprovalQueue:
    queue = []

    @classmethod
    def add(cls, request):

        cls.queue.append(request)

    @classmethod
    def get_all(cls):

        return cls.queue

    @classmethod
    def find_by_id(cls, request_id):

        for request in cls.queue:
            if request.request_id == request_id:
                return request

        return None

    @classmethod
    def get_pending(cls):

        return [request for request in cls.queue if request.status == "pending"]

    @classmethod
    def get_approved(cls):

        return [request for request in cls.queue if request.status == "approved"]

    @classmethod
    def get_rejected(cls):

        return [request for request in cls.queue if request.status == "rejected"]
