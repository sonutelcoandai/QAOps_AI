from mcp.adapters.base_adapter import BaseAdapter


class JiraAdapter(BaseAdapter):
    def transform(self, request):

        return {"system": "jira", "payload": request}
