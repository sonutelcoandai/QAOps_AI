from mcp.load_mcp import load_mcp

from mcp.routing.mcp_router import MCPRouter

load_mcp()

server = MCPRouter.get_server("mock")

print(server.execute({"action": "health_check"}))
