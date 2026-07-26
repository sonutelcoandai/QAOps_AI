from mcp.clients.jira_client import JiraClient

from mcp.clients.confluence_client import ConfluenceClient

from mcp.clients.github_client import GitHubClient

from mcp.clients.azure_devops_client import AzureDevOpsClient

from mcp.clients.postman_client import PostmanClient


clients = {
    "jira": JiraClient(),
    "confluence": ConfluenceClient(),
    "github": GitHubClient(),
    "azure_devops": AzureDevOpsClient(),
    "postman": PostmanClient(),
}


def get_client(client_name):

    return clients.get(client_name)
