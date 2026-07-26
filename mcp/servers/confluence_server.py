from mcp.servers.base_server import BaseServer


class ConfluenceServer(BaseServer):
    def execute(self, request):

        return {"server": "confluence", "request": request, "status": "completed"}
