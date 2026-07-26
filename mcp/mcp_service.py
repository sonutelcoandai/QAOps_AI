from mcp.routing.mcp_router import MCPRouter


class MCPService:
    @staticmethod
    def execute(server_name, request):

        server = MCPRouter.get_server(server_name)

        return server.execute(request)
