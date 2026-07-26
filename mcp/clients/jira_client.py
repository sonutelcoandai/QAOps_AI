from mcp.clients.base_client import BaseClient


class JiraClient(BaseClient):
    def connect(self):

        return True

    def execute(self, request):

        return {"client": "jira", "request": request, "status": "completed"}
