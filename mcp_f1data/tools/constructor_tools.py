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
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier")
        ) -> json:
            """
            Get constructor information:
                id, str
                name, str
                full_name, str
                country, str
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/{constructor_id}")
            return result

        @mcp.tool(name="get_constructor_chronology")
        async def get_constructor_chronology(
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier")
        ) -> json:
            """
            Get constructor's F1 chronology list F1 history of specific constructor:
                id, str
                name, str
                full_name, str
                country, str
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/{constructor_id}/chronology")
            return result

        @mcp.tool(name="get_constructor_drivers")
        async def get_constructor_drivers(
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier")
        ) -> json:
            """
            Get constructor's F1 drivers list F1 history of specific constructor:
                engine_manufacturer_id, str
                constructor_id, str
                year, int
                rounds", str
                entrant, obj
                driver, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{constructor_id}/drivers")
            return result

        @mcp.tool(name="get_constructor_drivers_by_season")
        async def get_constructor_drivers_by_season(
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier"),
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get constructor's F1 drivers list about one constructor in specific season:
                engine_manufacturer_id, str
                constructor_id, str
                year, int
                rounds", str
                entrant, obj
                driver, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{constructor_id}/{year}/drivers")
            return result