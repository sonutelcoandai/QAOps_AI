from mcp.load_mcp import load_mcp

from mcp.registry.mcp_registry import MCPRegistry

load_mcp()

for server_name in [
    "jira_server",
    "confluence_server",
    "github_server",
    "azure_devops_server",
    "postman_server",
]:
    server = MCPRegistry.get(server_name)

    print(server.execute({"action": "health_check"}))
