from mcp.mcp_gateway import MCPGateway


class MCPToolService:
    @staticmethod
    def create_jira_ticket(summary):

        return MCPGateway.execute({"action": "create_ticket", "summary": summary})

    @staticmethod
    def create_github_pr(title):

        return MCPGateway.execute({"action": "create_pr", "title": title})

    @staticmethod
    def create_confluence_page(title):

        return MCPGateway.execute({"action": "create_page", "title": title})

    @staticmethod
    def create_azure_work_item(title):

        return MCPGateway.execute({"action": "create_work_item", "title": title})

    @staticmethod
    def run_postman_collection(collection):

        return MCPGateway.execute(
            {"action": "run_collection", "collection": collection}
        )
