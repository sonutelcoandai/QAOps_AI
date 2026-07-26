class PerformanceResult:
    def __init__(self, status, virtual_users, response_time):

        self.status = status
        self.virtual_users = virtual_users
        self.response_time = response_time

    def to_dict(self):

        return {
            "status": self.status,
            "virtual_users": self.virtual_users,
            "response_time": self.response_time,
        }
