from mcp.clients.base_client import BaseClient


class ConfluenceClient(BaseClient):
    def connect(self):

        return True

    def execute(self, request):

        return {"client": "confluence", "request": request, "status": "completed"}
