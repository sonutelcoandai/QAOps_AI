from self_healing.healing_policy import HealingPolicy

from self_healing.healing_result import HealingResult

from self_healing.locator_healing.locator_healing_service import LocatorHealingService

from self_healing.api_healing.api_healing_service import APIHealingService

from self_healing.workflow_healing.workflow_healing_service import (
    WorkflowHealingService,
)

from self_healing.test_healing.test_healing_service import TestHealingService


class HealingService:
    @staticmethod
    def heal(failure_type, data=None):

        action = HealingPolicy.get_action(failure_type)

        if failure_type == "locator" and data:
            return {
                "healed": True,
                "action": action,
                "details": LocatorHealingService.heal(data),
            }

        if failure_type == "api" and data:
            return {
                "healed": True,
                "action": action,
                "details": APIHealingService.heal(data),
            }

        if failure_type == "workflow" and data:
            return {
                "healed": True,
                "action": action,
                "details": WorkflowHealingService.heal(data),
            }

        if failure_type == "test" and data:
            return {
                "healed": True,
                "action": action,
                "details": TestHealingService.heal(data),
            }

        result = HealingResult(healed=True, action=action)

        return result.to_dict()
