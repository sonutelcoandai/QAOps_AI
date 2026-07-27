class LocatorHealingResult:
    def __init__(self, original_locator, healed_locator, healed):

        self.original_locator = original_locator
        self.healed_locator = healed_locator
        self.healed = healed

    def to_dict(self):

        return {
            "original_locator": self.original_locator,
            "healed_locator": self.healed_locator,
            "healed": self.healed,
        }
