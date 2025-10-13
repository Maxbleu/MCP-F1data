from fastmcp import FastMCP
from abc import abstractmethod

class BaseTools:
    def __init__(self, mcp: FastMCP):
        self.mcp = mcp

    @classmethod
    @abstractmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """
        Register all tools with the MCP server.
        Must be implemented by all subclasses.
        
        Args:
            mcp: FastMCP instance to register tools with
        """

        pass