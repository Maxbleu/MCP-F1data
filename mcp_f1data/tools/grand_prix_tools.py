import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class GrandPrixTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/grand_prix"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all grand prix tools with MCP"""

        @mcp.tool(name="search_grand_prix")
        async def search_grand_prix(
            grand_prix: str = Field(title="grand_prix", description="Grand Prix's name. Eg: Japan GP, SÃ£o Paulo GP")
        ) -> json:
            """
            Get grand prix historical information.
            Use it when you are searching only one:
                abbreviation, str
                name, str
                total_races_held, int
                short_name, str
                id, str
                full_name, str
                country_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/search",data={"grand_prix":grand_prix})
            return result

        @mcp.tool(name="get_grand_prix_by_id_and_year")
        async def get_grand_prix_by_id_and_year(
            grand_prix_id: str = Field(title="grand_prix_id", description="Grand Prix's identifier"),
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get grand prix of especific season:
                date, str
                drivers_championship_decider, bool
                qualifying_1_time, str
                sprint_race_time, str
                time, str
                direction, str
                constructors_championship_decider, bool
                free_practice_2_date, date
                qualifying_2_date, date
                warming_up_date, date
                official_name, str
                course_length, float
                pre_qualifying_date, date
                free_practice_2_time, str
                qualifying_2_time, str
                warming_up_time, str
                year, int
                turns, int
                free_practice_3_date, date
                qualifying_date, date
                qualifying_format, str
                laps, int
                pre_qualifying_time, str
                free_practice_3_time, str
                qualifying_time, str
                id, int
                circuit_type, str
                distance, float
                free_practice_4_date, date
                sprint_qualifying_date, date
                round, int
                scheduled_laps, int
                free_practice_1_date, date
                free_practice_4_time, str
                sprint_qualifying_time, str
                scheduled_distance, float
                free_practice_1_time, str
                qualifying_1_date, date
                sprint_race_date, date
                grand_prix, obj
                circuit, ob
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{grand_prix_id}/{year}")
            return result

        @mcp.tool(name="get_grand_prix_chronology_by_id")
        async def get_grand_prix_chronology_by_id(
            grand_prix_id: str = Field(title="grand_prix_id", description="Grand Prix's identifier")
        ) -> json:
            """
            Get a list of specific F1 Grands Prix held at circuits at long of F1 history:
                date, str
                drivers_championship_decider, bool
                qualifying_1_time, str
                sprint_race_time, str
                time, str
                direction, str
                constructors_championship_decider, bool
                free_practice_2_date, date
                qualifying_2_date, date
                warming_up_date, date
                official_name, str
                course_length, float
                pre_qualifying_date, date
                free_practice_2_time, str
                qualifying_2_time, str
                warming_up_time, str
                year, int
                turns, int
                free_practice_3_date, date
                qualifying_date, date
                qualifying_format, str
                laps, int
                pre_qualifying_time, str
                free_practice_3_time, str
                qualifying_time, str
                id, int
                circuit_type, str
                distance, float
                free_practice_4_date, date
                sprint_qualifying_date, date
                round, int
                scheduled_laps, int
                free_practice_1_date, date
                free_practice_4_time, str
                sprint_qualifying_time, str
                scheduled_distance, float
                free_practice_1_time, str
                qualifying_1_date, date
                sprint_race_date, date
                grand_prix, obj
                circuit, ob
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{grand_prix_id}/chronology")
            return result

        @mcp.tool(name="get_grand_prix_drivers_championship_decider_by_id")
        async def get_grand_prix_drivers_championship_decider_by_id(
            grand_prix_id: str = Field(title="grand_prix_id", description="Grand Prix's identifier")
        ) -> json:
            """
            Get a list of F1 Grands Prix held at different circuits that decided the Constructors' Championship:
                date, str
                drivers_championship_decider, bool
                qualifying_1_time, str
                sprint_race_time, str
                time, str
                direction, str
                constructors_championship_decider, bool
                free_practice_2_date, date
                qualifying_2_date, date
                warming_up_date, date
                official_name, str
                course_length, float
                pre_qualifying_date, date
                free_practice_2_time, str
                qualifying_2_time, str
                warming_up_time, str
                year, int
                turns, int
                free_practice_3_date, date
                qualifying_date, date
                qualifying_format, str
                laps, int
                pre_qualifying_time, str
                free_practice_3_time, str
                qualifying_time, str
                id, int
                circuit_type, str
                distance, float
                free_practice_4_date, date
                sprint_qualifying_date, date
                round, int
                scheduled_laps, int
                free_practice_1_date, date
                free_practice_4_time, str
                sprint_qualifying_time, str
                scheduled_distance, float
                free_practice_1_time, str
                qualifying_1_date, date
                sprint_race_date, date
                grand_prix, obj
                circuit, ob
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{grand_prix_id}/championship_decider/drivers")
            return result

        @mcp.tool(name="get_grand_prix_constructors_championship_decider_by_id")
        async def get_grand_prix_constructors_championship_decider_by_id(
            grand_prix_id: str = Field(title="grand_prix_id", description="Grand Prix's identifier")
        ) -> json:
            """
            Get a list of F1 Grands Prix held at different circuits that decided the Constructors' Championship:
                date, str
                drivers_championship_decider, bool
                qualifying_1_time, str
                sprint_race_time, str
                time, str
                direction, str
                constructors_championship_decider, bool
                free_practice_2_date, date
                qualifying_2_date, date
                warming_up_date, date
                official_name, str
                course_length, float
                pre_qualifying_date, date
                free_practice_2_time, str
                qualifying_2_time, str
                warming_up_time, str
                year, int
                turns, int
                free_practice_3_date, date
                qualifying_date, date
                qualifying_format, str
                laps, int
                pre_qualifying_time, str
                free_practice_3_time, str
                qualifying_time, str
                id, int
                circuit_type, str
                distance, float
                free_practice_4_date, date
                sprint_qualifying_date, date
                round, int
                scheduled_laps, int
                free_practice_1_date, date
                free_practice_4_time, str
                sprint_qualifying_time, str
                scheduled_distance, float
                free_practice_1_time, str
                qualifying_1_date, date
                sprint_race_date, date
                grand_prix, obj
                circuit, ob
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{grand_prix_id}/championship_decider/constructors")
            return result