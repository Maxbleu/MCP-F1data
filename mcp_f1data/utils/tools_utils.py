from fastmcp import FastMCP

def load_tools(self, mcp: FastMCP):
    metodos = [m for m in dir(self) if callable(getattr(self, m)) and not m.startswith('__')]
    for nombre in metodos:
        funcion = getattr(self, nombre)
        mcp.tool(
            funcion,
            name=nombre,
            description=getattr(funcion, "__doc__", "No description provided"),
            annotations=getattr(funcion, "__annotations__", {})
        )