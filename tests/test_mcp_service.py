from orchestration.platform_bootstrap import PlatformBootstrap

from mcp.mcp_service import MCPService

PlatformBootstrap.initialize()

result = MCPService.execute("mock", {"action": "health_check"})

print(result)
