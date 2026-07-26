from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.telecom_intelligence_hub import TelecomIntelligenceHub

PlatformBootstrap.initialize()

result = TelecomIntelligenceHub.ask("Validate TMF641 billing integration")

print(result)
