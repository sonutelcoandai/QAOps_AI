from mcp.clients.base_client import BaseClient


class PostmanClient(BaseClient):
    def connect(self):

        return True

    def execute(self, request):

        return {"client": "postman", "request": request, "status": "completed"}
