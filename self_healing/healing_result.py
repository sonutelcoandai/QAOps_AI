class HealingResult:
    def __init__(self, healed, action):

        self.healed = healed
        self.action = action

    def to_dict(self):

        return {"healed": self.healed, "action": self.action}
