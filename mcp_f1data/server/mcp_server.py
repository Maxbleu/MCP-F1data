import os
from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier
from ..tools.f1data_tools import register_f1data_tools

def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server"""

    auth = JWTVerifier(
        public_key=os.getenv("PUBLIC_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )

    mcp = FastMCP(
        name="mcp-f1data",
        auth=auth
    )

    register_f1data_tools(mcp)
    return mcp

def main():
    """Main function for local development"""
    mcp = create_mcp_server()

    if os.getenv("RAILWAY_ENVIRONMENT"):
        port = int(os.getenv("PORT", 8000))
        mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
    else:
        mcp.run()