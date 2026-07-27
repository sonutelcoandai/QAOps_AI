from self_healing.api_healing.api_healing_result import APIHealingResult


class APIHealingService:
    @staticmethod
    def heal(endpoint):

        healed_endpoint = f"{endpoint}/v2"

        result = APIHealingResult(
            endpoint=endpoint, healed_endpoint=healed_endpoint, healed=True
        )

        return result.to_dict()
