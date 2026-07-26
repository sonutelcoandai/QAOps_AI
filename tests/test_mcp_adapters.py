from mcp.adapters.github_adapter import GitHubAdapter

from mcp.adapters.jira_adapter import JiraAdapter

print(GitHubAdapter().transform({"action": "create_pr"}))

print(JiraAdapter().transform({"action": "create_ticket"}))
