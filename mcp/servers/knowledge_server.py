from mcp.servers.base_server import BaseServer

from knowledge.knowledge_query_service import KnowledgeQueryService


class KnowledgeServer(BaseServer):
    def execute(self, request):

        query = request.get("query", "")

        result = KnowledgeQueryService.ask(query)

        return {"server": "knowledge", "query": query, "response": result}
