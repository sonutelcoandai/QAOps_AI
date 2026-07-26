from mcp.routing.request_router import RequestRouter


class MCPGateway:
    @staticmethod
    def execute(request):

        return RequestRouter.route(request)
