class APIResult:
    def __init__(self, status, response_data, response_code):

        self.status = status

        self.response_data = response_data

        self.response_code = response_code

    def to_dict(self):

        return {
            "status": self.status,
            "response_code": self.response_code,
            "response_data": self.response_data,
        }
