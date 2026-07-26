from mcp.adapters.base_adapter import BaseAdapter


class AzureDevOpsAdapter(BaseAdapter):
    def transform(self, request):

        return {"system": "azure_devops", "payload": request}
