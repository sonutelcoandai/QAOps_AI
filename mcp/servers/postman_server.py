from mcp.servers.base_server import BaseServer


class PostmanServer(BaseServer):
    def execute(self, request):

        return {"server": "postman", "request": request, "status": "completed"}
