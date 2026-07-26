from mcp.servers.base_server import BaseServer


class GitHubServer(BaseServer):
    def execute(self, request):

        return {"server": "github", "request": request, "status": "completed"}
