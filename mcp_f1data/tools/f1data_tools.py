from fastmcp import FastMCP
from .execution_tools import ExecutionTools

def register_f1data_tools(mcp:FastMCP):
    """Register all F1 tools with the MCP server"""

    ExecutionTools.__register_mcp_tools__(mcp=mcp)