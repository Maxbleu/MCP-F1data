import os
from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier
from ..tools.f1data_tools import register_f1data_tools

def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server"""

    auth = JWTVerifier(
        public_key="-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu1SU1LfVLPHCozMxH2Mo4lgOEePzNm0tRgeLezV6ffAt0gunVTLw7onLRnrq0/IzW7yWR7QkrmBL7jTKEn5u+qKhbwKfBstIs+bMY2Zkp18gnTxKLxoS2tFczGkPLPgizskuemMghRniWaoLcyehkd3qqGElvW/VDL5AaWTg0nLVkjRo9z+40RQzuVaE8AkAFmxZzow3x+VJYKdjykkJ0iT9wCS0DRTXu269V264Vf/3jvredZiKRkgwlL9xNAwxXFg0x/XFw005UWVRIkdgcKWTjpBP2dPwVZ4WWC+9aGVd+Gyn1o0CLelf4rEjGoXbAAEgAqeGUxrcIlbjXfbcmwIDAQAB-----END PUBLIC KEY-----",
        algorithm="RS256"
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