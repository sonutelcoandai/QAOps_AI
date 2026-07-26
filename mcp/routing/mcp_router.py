from mcp.registry.mcp_registry import MCPRegistry


class MCPRouter:
    @staticmethod
    def get_server(server_name):

        server = MCPRegistry.get(server_name)

        if server is None:
            raise ValueError(f"MCP Server '{server_name}' not found")

        return server
