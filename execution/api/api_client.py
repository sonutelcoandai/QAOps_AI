class APIClient:
    def execute(self, endpoint, method="GET", payload=None):

        return {
            "endpoint": endpoint,
            "method": method,
            "payload": payload,
            "mock": True,
        }
