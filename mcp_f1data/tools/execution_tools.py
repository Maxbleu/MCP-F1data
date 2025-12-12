from io import StringIO
import json, sys, traceback
from fastmcp import FastMCP
from datetime import datetime
from .race_tools import RaceTools
from .season_tools import SeasonTools
from .driver_tools import DriverTools
from .circuit_tools import CircuitTools
from .grand_prix_tools import GrandPrixTools
from .constructor_tools import ConstructorTools
from .manufacturer_tools import ManufacturerTools

class ExecutionTools:
    @staticmethod
    def execute_code(code: str) -> str:
        """
        Execute Python code that can use the F1 data tools.
        """
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            # Define the environment with available tools
            env = {
                "json": json,
                "DriverTools": DriverTools,
                "RaceTools": RaceTools,
                "SeasonTools": SeasonTools,
                "CircuitTools": CircuitTools,
                "GrandPrixTools": GrandPrixTools,
                "ConstructorTools": ConstructorTools,
                "ManufacturerTools": ManufacturerTools,
            }
            
            # Add individual functions to env for convenience
            tool_classes = [
                DriverTools, RaceTools, SeasonTools, CircuitTools, 
                GrandPrixTools, ConstructorTools, ManufacturerTools
            ]
            
            for tool_cls in tool_classes:
                for attr_name in dir(tool_cls):
                    attr = getattr(tool_cls, attr_name)
                    if isinstance(attr, staticmethod) or (callable(attr) and not attr_name.startswith("_")):
                            env[attr_name] = attr

            local_env = {}
            exec(code, env, local_env)

            output = sys.stdout.getvalue()

            if "result" in local_env:
                result_value = local_env["result"]
                if isinstance(result_value, (dict, list)):
                    return json.dumps(result_value, indent=2, default=str)
                return str(result_value)
            elif output:
                return output.strip()
                
            return "Execution successful. Define a variable named 'result' to return data."
        except KeyError as e:
            # ← AQUÍ CAPTURAMOS el KeyError: 0
            return f"❌ KeyError: Cannot access key/index {e}.\n\nPossible causes:\n- Trying to access dicts[{e}] when dicts is empty\n- Dictionary missing key '{e}'\n\nGenerated code:\n{code}\n\nTip: Add validation like 'if dicts and len(dicts) > 0' before accessing."
        
        except IndexError as e:
            return f"❌ IndexError: {str(e)}\n\nTrying to access an index that doesn't exist.\n\nCode:\n{code}"
        
        except Exception as e:
            tb = traceback.format_exc()
            return f"❌ Error executing code:\n{type(e).__name__}: {str(e)}\n\nFull traceback:\n{tb}\n\nCode that failed:\n{code}"
        
        finally:
            sys.stdout = old_stdout

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register execution tools with MCP"""

        @mcp.tool(name="execute_python")
        async def execute_python(
            code: str,
            year: int = datetime.now().year,
            input: str = "",
            toolCallId: str = ""
        ) -> str:
            """
            Execute Python code that can use the F1 data tools.
            The following tools are available as functions in the environment:
            
            - DriverTools: search_driver, get_driver_family_relationship_by_id, get_driver_career_by_id
            - RaceTools: get_free_practice_1_by_id, get_race_result_by_id, etc.
            - SeasonTools: get_season_constructors_by_year, etc.
            - CircuitTools: search_circuit, get_circuit_chronology_by_id, etc.
            - GrandPrixTools: search_grand_prix, get_grand_prix_chronology_by_id, etc.
            - ConstructorTools: search_constructor, get_constructor_chronology, etc.
            - ManufacturerTools: search_tyre_manufacturer, search_engine_manufacturer
            
            You can call these functions directly, e.g., search_driver("Hamilton") or RaceTools.get_race_result_by_id(123).
            The functions return JSON data (dicts or lists).
            """
            return cls.execute_code(code)
