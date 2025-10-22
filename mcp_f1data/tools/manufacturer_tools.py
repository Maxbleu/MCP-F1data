import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class ManufacturerTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/manufacturers"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all manufacturer tools with MCP"""

        @mcp.tool(name="get_tyres_manufacturer_by_id")
        async def get_tyres_manufacturer_by_id(
            tyre_manufacturer_id: str = Field(title="tyre_manufacturer_id", description="Tyre manufacturer's identifier")
        ) -> json:
            """
            Get stats tyre manufacturer along of F1 history:
                id, str
                name, str
                country_id, str
                best_starting_grid_position, int
                best_race_result, int
                total_race_entries, int
                total_race_starts, int
                total_race_wins, int
                total_race_laps, int
                total_podiums, int
                total_podium_races, int
                total_pole_positions, int
                total_fastest_laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/tyres/{tyre_manufacturer_id}")
            return result

        @mcp.tool(name="get_engine_manufacturer_by_id")
        async def get_engine_manufacturer_by_id(
            engine_manufacturer_id: str = Field(title="engine_manufacturer_id", description="Engine manufacturer's identifier")
        ) -> json:
            """
            Get stats engine manufacturer along of F1 history:
                id, str
                name, str
                country_id, str
                best_championship_position, int
                best_starting_grid_position, int
                best_race_result, int
                total_race_entries, int
                total_race_starts, int
                total_race_wins, int
                total_race_laps, int
                total_podiums, int
                total_podium_races, int
                total_points, float
                total_championship_points, float
                total_pole_positions, int
                total_fastest_laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/engines/{engine_manufacturer_id}")
            return result