from fastmcp import FastMCP
from abc import abstractmethod

class BaseTools:
    def __init__(self, mcp_instance: FastMCP, base_path:str=""):
        self.__BASE_PATH__ = base_path
        self.mcp = mcp_instance

    __BASE_PATH__ = ""

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