from mcp.load_mcp import load_mcp

from mcp.mcp_knowledge_service import MCPKnowledgeService

load_mcp()

result = MCPKnowledgeService.search("TMF641 Service Order")

print(result)
