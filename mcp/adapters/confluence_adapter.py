from mcp.adapters.base_adapter import BaseAdapter


class ConfluenceAdapter(BaseAdapter):
    def transform(self, request):

        return {"system": "confluence", "payload": request}
