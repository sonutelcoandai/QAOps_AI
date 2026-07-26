from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.telecom_query_service import TelecomQueryService

PlatformBootstrap.initialize()

result = TelecomQueryService.execute("Validate TMF641 Service Order API")

print(result)
