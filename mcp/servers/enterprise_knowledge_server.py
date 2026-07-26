from mcp.servers.base_server import BaseServer


class EnterpriseKnowledgeServer(BaseServer):
    def execute(self, request):

        query = request.get("query", "")

        return {
            "server": "enterprise_knowledge",
            "query": query,
            "sources": ["confluence", "github", "internal_knowledge"],
            "status": "completed",
        }
