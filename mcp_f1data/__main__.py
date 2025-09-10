"""
Entry point for running the F1Data MCP server as a module.
This allows: python -m mcp_f1data
"""

from .server.mcp_server import main

if __name__ == "__main__":
    main()