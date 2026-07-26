from mcp.servers.base_server import BaseServer


class JiraServer(BaseServer):
    def execute(self, request):

        return {"server": "jira", "request": request, "status": "completed"}
