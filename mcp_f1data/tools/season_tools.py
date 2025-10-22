import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class SeasonTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/seasons"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all season tools with MCP"""

        @mcp.tool(name="get_season_constructors_by_year")
        async def get_season_constructors_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get list of every entrant constructor of the season:
                engine_manufacturer_id, str
                year, int
                constructor, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/constructors")
            return result

        @mcp.tool(name="get_season_constructors_by_year_and_constructor_id")
        async def get_season_constructors_by_year_and_constructor_id(
            year: int = Field(title="year", description="Year of the season"),
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier")
        ) -> json:
            """
            Get a specific constructor of the season:
                engine_manufacturer_id, str
                year, int
                constructor, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/constructors/{constructor_id}")
            return result

        @mcp.tool(name="get_season_drivers_by_year")
        async def get_season_drivers_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get list of every entrant drivers of the season:
                constructor_id, str
                engine_manufacturer_id, str
                year, int
                rounds, str
                entrant, obk
                driver, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/drivers")
            return result

        @mcp.tool(name="get_season_drivers_by_year_and_driver_id")
        async def get_season_drivers_by_year_and_driver_id(
            year: int = Field(title="year", description="Year of the season"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a specific driver of the season:
                constructor_id, str
                engine_manufacturer_id, str
                year, int
                rounds, str
                entrant, obk
                driver, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/drivers/{driver_id}")
            return result

        @mcp.tool(name="get_season_tyres_by_year")
        async def get_season_tyres_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get a list of every tyre's stats of the season:
                best_starting_grid_position, int
                total_race_entries, int
                year, int
                tyre_manufacturer_id, str
                total_race_wins, int
                total_podiums, int
                total_pole_positions, int
                best_race_result, int
                total_race_starts, int
                total_race_laps, int
                total_podium_races, int
                total_fastest_laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/tyres/stats")
            return result

        @mcp.tool(name="get_season_engines_by_year")
        async def get_season_engines_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get a list of every engine's stats of the season:
                best_starting_grid_position, int
                total_race_entries, int
                year, int
                engine_manufacturer_id, str
                total_race_wins, int
                total_podiums, int
                total_pole_positions, int
                best_race_result, int
                total_race_starts, int
                total_race_laps, int
                total_podium_races, int
                total_fastest_laps, int
                total_points, float
                position_number, int
                position_text, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/engines/stats")
            return result

        @mcp.tool(name="get_season_chassis_by_year")
        async def get_season_chassis_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get a list of every constructor's chassis of the season:
                year, int
                engine_manufacturer_id, str
                entrant, obj
                chassis, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/chassis")
            return result

        @mcp.tool(name="get_season_driver_standing_by_year")
        async def get_season_driver_standing_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get a list of drivers standing of the season:
                driver_id, str
                year, int
                position_display_order, int
                position_number, int
                position_text, str
                points, float
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/standing/drivers")
            return result

        @mcp.tool(name="get_season_constructor_standing_by_year")
        async def get_season_constructor_standing_by_year(
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get a list of every constructor's chassis of the season:
                position_text, str
                year, int
                position_number, int
                engine_manufacturer_id, str
                constructor_id, str
                position_display_order, int
                points, float
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/standing/constructors")
            return result