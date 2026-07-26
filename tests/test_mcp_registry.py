from mcp.load_mcp import load_mcp

from mcp.registry.mcp_registry import MCPRegistry

load_mcp()

print()

print(MCPRegistry.get_all().keys())
