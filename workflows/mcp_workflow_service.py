from mcp.mcp_tool_service import MCPToolService


class MCPWorkflowService:
    @staticmethod
    def create_defect(summary):

        return MCPToolService.create_jira_ticket(summary)

    @staticmethod
    def create_pull_request(title):

        return MCPToolService.create_github_pr(title)

    @staticmethod
    def create_documentation(title):

        return MCPToolService.create_confluence_page(title)

    @staticmethod
    def run_api_tests(collection):

        return MCPToolService.run_postman_collection(collection)
