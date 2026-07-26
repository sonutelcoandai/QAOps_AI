from mcp.load_clients import get_client

for client_name in ["jira", "confluence", "github", "azure_devops", "postman"]:
    client = get_client(client_name)

    result = client.execute({"action": "health_check"})

    print(result)
