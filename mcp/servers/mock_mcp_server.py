from mcp.base_mcp import BaseMCP


class MockMCPServer(BaseMCP):
    def connect(self):

        return True

    def execute(self, request):

        return {"server": "mock", "request": request, "status": "completed"}
