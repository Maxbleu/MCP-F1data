import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class EntrantTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/entrants"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all entrants tools with MCP"""

        @mcp.tool(name="get_season_entrant_constructors_by_year")
        async def get_season_entrant_constructors_by_year(
            year: int = Field(description="Season's year")
        ) -> json:
            """
            Get constructors entrant of specific season:
                year, int
                engine_manufacturer_id, str
                constructor, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/constructors")
            return result

        @mcp.tool(name="get_season_entrant_chassis_by_year_and_entrant_id")
        async def get_season_entrant_chassis_by_year_and_entrant_id(
            year: int = Field(description="Season's year"),
            entrant_id: str = Field(description="Entrant identifier")
        ) -> json:
            """
            Get chassis of specific entrant in specific year:
                year, int
                engine_manufacturer_id, str
                entrant, obj
                chassis, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{entrant_id}/chassis")
            return result

        @mcp.tool(name="get_season_entrant_drivers_by_year")
        async def get_season_entrant_drivers_by_year(
            year: int = Field(description="Season's year")
        ) -> json:
            """
            Get drivers of specific season:
                year, int
                constructor_id, str
                rounds, str
                engine_manufacturer_id, str
                driver, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/drivers")
            return result

        @mcp.tool(name="get_season_entrant_drivers_by_year_and_entrant_id")
        async def get_season_entrant_drivers_by_year_and_entrant_id(
            year: int = Field(description="Season's year"),
            entrant_id: str = Field(description="Entrant identifier")
        ) -> json:
            """
            Get drivers of specific entrant of one year:
                year, int
                constructor_id, str
                rounds, str
                engine_manufacturer_id, str
                driver, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{entrant_id}/drivers")
            return result

        @mcp.tool(name="get_season_entrant_engines_by_year_and_entrant_id")
        async def get_season_entrant_engines_by_year_and_entrant_id(
            year: int = Field(description="Season's year"),
            entrant_id: str = Field(description="Entrant identifier")
        ) -> json:
            """
            Get engines of specific season of specific entrant:
                engine_manufacturer_id, str
                year, int
                constructor_id, str
                entrant, obj
                engine, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{entrant_id}/engines")
            return result

        @mcp.tool(name="get_season_entrant_tyres_by_year_and_entrant_id")
        async def get_season_entrant_tyres_by_year_and_entrant_id(
            year: int = Field(description="Season's year"),
            entrant_id: str = Field(description="Entrant identifier")
        ) -> json:
            """
            Get tyres of specific season of specific entrant:
                year, int
                tyre_manufacturer_id, str
                constructor_id, str
                engine_manufacturer_id, str
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{entrant_id}/tyres")
            return result

        @mcp.tool(name="get_season_entrant_cars_by_year_and_entrant_id")
        async def get_season_entrant_cars_by_year_and_entrant_id(
            year: int = Field(description="Season's year"),
            entrant_id: str = Field(description="Entrant identifier")
        ) -> json:
            """
            Get cars of specific year of specific entrant:
                year, int
                engine_list, json
                chassis_list, json
                tyres_list, json
                driver_list, json
                constructor, obj
                entrant, obj
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{entrant_id}/cars")
            return result