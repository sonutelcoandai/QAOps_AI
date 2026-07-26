from mcp.load_mcp import load_mcp


class MCPBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing MCP Layer...\n")

        load_mcp()

        print("MCP Layer Ready")

        print()
