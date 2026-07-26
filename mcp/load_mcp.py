from mcp.registry.mcp_registry import MCPRegistry

from mcp.servers.mock_mcp_server import MockMCPServer

from mcp.clients.jira_client import JiraClient

from mcp.clients.confluence_client import ConfluenceClient

from mcp.clients.github_client import GitHubClient

from mcp.clients.azure_devops_client import AzureDevOpsClient

from mcp.clients.postman_client import PostmanClient

from mcp.servers.jira_server import JiraServer
from mcp.servers.confluence_server import ConfluenceServer
from mcp.servers.github_server import GitHubServer
from mcp.servers.azure_devops_server import AzureDevOpsServer
from mcp.servers.postman_server import PostmanServer
from mcp.servers.knowledge_server import KnowledgeServer
from mcp.servers.enterprise_knowledge_server import EnterpriseKnowledgeServer


def load_mcp():

    # MCP Server

    MCPRegistry.register("mock", MockMCPServer())
    MCPRegistry.register("jira_server", JiraServer())

    MCPRegistry.register("confluence_server", ConfluenceServer())

    MCPRegistry.register("github_server", GitHubServer())

    MCPRegistry.register("azure_devops_server", AzureDevOpsServer())

    MCPRegistry.register("postman_server", PostmanServer())

    MCPRegistry.register("knowledge_server", KnowledgeServer())
    MCPRegistry.register("enterprise_knowledge_server", EnterpriseKnowledgeServer())

    print("MCP Server Loaded: mock")

    # MCP Clients

    MCPRegistry.register("jira", JiraClient())

    print("MCP Client Loaded: jira")

    MCPRegistry.register("confluence", ConfluenceClient())

    print("MCP Client Loaded: confluence")

    MCPRegistry.register("github", GitHubClient())

    print("MCP Client Loaded: github")

    MCPRegistry.register("azure_devops", AzureDevOpsClient())

    print("MCP Client Loaded: azure_devops")

    MCPRegistry.register("postman", PostmanClient())

    print("MCP Client Loaded: postman")
