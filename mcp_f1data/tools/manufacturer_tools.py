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

        @mcp.tool(name="search_tyre_manufacturer")
        async def search_tyre_manufacturer(
            tyre_manufacturer: str = Field(title="tyre_manufacturer", description="Tyre manufacturer's name")
        ) -> json:
            """
            Search a scpecific tyre manufacturer along of F1 history.
            Use it when you are searching only one:
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/tyres/search",data={"tyre_manufacturer":tyre_manufacturer})
            return result

        @mcp.tool(name="search_engine_manufacturer")
        async def search_engine_manufacturer(
            engine_manufacturer: str = Field(title="engine_manufacturer", description="Engine manufacturer's name")
        ) -> json:
            """
            Search a scpecific engine manufacturer along of F1 history.
            Use it when you are searching only one:
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/engines/search", data={"engine_manufacturer":engine_manufacturer})
            return result