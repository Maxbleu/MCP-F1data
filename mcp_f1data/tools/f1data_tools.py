from fastmcp import FastMCP
from .driver_tools import DriverTools
from .telemetry_tools import TelemetryTools
from .constructor_tools import ConstructorTools
from .circuit_tools import CircuitTools
from .grand_prix_tools import GrandPrixTools

def register_f1data_tools(mcp:FastMCP):
    """Register all F1 tools with the MCP server"""

    TelemetryTools.__register_mcp_tools__(mcp=mcp)
    DriverTools.__register_mcp_tools__(mcp=mcp)
    ConstructorTools.__register_mcp_tools__(mcp=mcp)
    CircuitTools.__register_mcp_tools__(mcp=mcp)
    GrandPrixTools.__register_mcp_tools__(mcp=mcp)