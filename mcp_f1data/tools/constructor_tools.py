import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class ConstructorTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/constructors"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all constructor tools with MCP"""

        @mcp.tool(name="get_constructor_by_id")
        async def get_constructor_by_id(
            constructor_id: str = Field(description="Constructor's identifier")
        ) -> json:
            """
            Get constructor information:
                id, str
                name, str
                full_name, str
                country_id, str
                best_championship_position, int
                best_race_result, int
                total_championship_wins, int
                total_race_entries, int
                total_race_start, int
                total_race_wins, int
                total_1_and_2_finishes, int
                total_race_laps, int
                total_podium_races, int
                total_points, float
                total_championship_points, float
                total_pole_position, int
                total_fastest_laps, int
            """
            result = launch_request_f1db(f"{cls._BASE_PATH}/{constructor_id}")
            return result

        @mcp.tool(name="get_constructor_chronology")
        async def get_constructor_chronology(
            constructor_id: str = Field(description="Constructor's identifier")
        ) -> json:
            """
            Get constructor's F1 chronology of specific constructor:
                constructor_id, str
                position_display_order, int
                other_constructor_id, str
                year_from, int
                year_to, int
            """
            result = launch_request_f1db(f"{cls._BASE_PATH}/{constructor_id}/chronology")
            return result