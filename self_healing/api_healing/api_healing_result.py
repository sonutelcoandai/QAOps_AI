class APIHealingResult:
    def __init__(self, endpoint, healed_endpoint, healed):

        self.endpoint = endpoint

        self.healed_endpoint = healed_endpoint

        self.healed = healed

    def to_dict(self):

        return {
            "endpoint": self.endpoint,
            "healed_endpoint": self.healed_endpoint,
            "healed": self.healed,
        }
