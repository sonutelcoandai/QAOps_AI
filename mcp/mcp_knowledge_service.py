from mcp.registry.mcp_registry import MCPRegistry


class MCPKnowledgeService:
    @staticmethod
    def search(query):

        server = MCPRegistry.get("enterprise_knowledge_server")

        return server.execute({"query": query})
