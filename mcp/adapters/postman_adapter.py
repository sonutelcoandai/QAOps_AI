from mcp.adapters.base_adapter import BaseAdapter


class PostmanAdapter(BaseAdapter):
    def transform(self, request):

        return {"system": "postman", "payload": request}
