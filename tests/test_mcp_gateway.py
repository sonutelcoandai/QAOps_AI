from mcp.mcp_gateway import MCPGateway

result = MCPGateway.execute(
    {"action": "create_ticket", "summary": "Billing validation issue"}
)

print(result)
