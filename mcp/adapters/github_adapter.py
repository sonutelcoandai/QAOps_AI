from mcp.adapters.base_adapter import BaseAdapter


class GitHubAdapter(BaseAdapter):
    def transform(self, request):

        return {"system": "github", "payload": request}
