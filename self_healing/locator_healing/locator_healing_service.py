from self_healing.locator_healing.locator_healing_result import LocatorHealingResult


class LocatorHealingService:
    @staticmethod
    def heal(locator):

        healed_locator = f"{locator}_healed"

        result = LocatorHealingResult(
            original_locator=locator, healed_locator=healed_locator, healed=True
        )

        return result.to_dict()
