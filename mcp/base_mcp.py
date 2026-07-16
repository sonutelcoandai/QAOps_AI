from abc import ABC, abstractmethod


class BaseMCP(ABC):
    @abstractmethod
    def connect(self):
        """
        Connect to MCP server
        """
        pass

    @abstractmethod
    def discover_tools(self):
        """
        Discover MCP tools
        """
        pass

    @abstractmethod
    def execute_tool(self, tool_name, payload):
        """
        Execute MCP tool
        """
        pass
