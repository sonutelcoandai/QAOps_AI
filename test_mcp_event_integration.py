import test_mcp_events

from mcp.mcp_tool_service import MCPToolService

print(MCPToolService.create_jira_ticket("TMF641 Validation Failed"))

print(MCPToolService.create_github_pr("TMF641 Fix"))

print(MCPToolService.run_postman_collection("TMF641 Collection"))
