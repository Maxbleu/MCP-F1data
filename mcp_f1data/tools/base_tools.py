from fastmcp import FastMCP
from ..utils import load_tools

class BaseTools:
    def __init__(self, mcp_instance: FastMCP, base_path:str=""):
        self.__BASE_PATH__ = base_path
        load_tools(self=self, mcp=mcp_instance)

    __BASE_PATH__ = ""

    @classmethod
    def __register_mcp_instance__(cls, mcp: FastMCP):
        cls(mcp)