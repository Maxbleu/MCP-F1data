import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class DriverTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp,base_path="/drivers")

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all driver tools with MCP"""

        @mcp.tool(name="get_driver_by_id")
        async def get_driver_by_id(
            driver_id: str = Field(description="Driver's identifier")
        ) -> json:
            """
            Get driver information:
                id, str
                name, str
                first_name, str
                last_name, str
                full_name, str
                abbreviation, str
                permanent_number, int
                gender, str
                date_of_birth, date
                date_of_death, date
                place_of_birth, str
                country_of_birth_country_id, str
                nationality_country_id, str
                second_nationality_country_id, str
                best_championship_position, int
                best_starting_grid_position, int
                best_race_result, int
                total_championship_wins, int
                total_race_entries, int
                total_race_starts, int
                total_race_wins, int
                total_race_laps, int
                total_podiums, int
                total_points, float
                total_championship_points, float
                total_pole_positions, int
                total_fastest_laps, int
                total_driver_of_the_day, int
                total_grand_slams, int
            """
            result = launch_request_f1db(f"/drivers/{driver_id}")
            return result

        @mcp.tool(name="get_driver_family_relationship")
        async def get_driver_family_relationship(
            driver_id: str = Field(description="Driver's identifier")
        ) -> json:
            """
            Get driver's F1 families of specific driver:
                driver_id, str
                position_display_order, int
                other_driver_id, str
                type, str
            """
            result = launch_request_f1db(f"/drivers/{driver_id}/family_relationship")
            return result