from fastmcp import FastMCP
from .driver_tools import DriverTools
from .telemetry_tools import TelemetryTools
from .constructor_tools import ConstructorTools
from .entrant_tools import EntrantTools

def register_f1data_tools(mcp:FastMCP):
    """Register all F1 tools with the MCP server"""

    TelemetryTools.__register_mcp_tools__(mcp=mcp)
    DriverTools.__register_mcp_tools__(mcp=mcp)
    ConstructorTools.__register_mcp_tools__(mcp=mcp)
    EntrantTools.__register_mcp_tools__(mcp=mcp)