from mcp.clients.base_client import BaseClient


class GitHubClient(BaseClient):
    def connect(self):

        return True

    def execute(self, request):

        return {"client": "github", "request": request, "status": "completed"}
