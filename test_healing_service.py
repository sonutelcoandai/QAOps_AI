from self_healing.healing_service import HealingService

print(HealingService.heal("locator"))

print(HealingService.heal("api"))

print(HealingService.heal("workflow"))

print(HealingService.heal("unknown"))
