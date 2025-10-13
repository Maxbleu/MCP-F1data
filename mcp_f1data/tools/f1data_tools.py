from fastmcp import FastMCP
from .driver_tools import DriverTools
from .telemetry_tools import TelemetryTools

def register_f1data_tools(mcp:FastMCP):
    """Register all F1 tools with the MCP server"""

    TelemetryTools.__register_mcp_tools__(mcp=mcp)
    DriverTools.__register_mcp_tools__(mcp=mcp)