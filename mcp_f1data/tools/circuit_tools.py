import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class CircuitTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/circuits"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all circuit tools with MCP"""

        @mcp.tool(name="get_circuit_by_id")
        async def get_circuit_by_id(
            circuit_id: str = Field(title="circuit_id", description="Circuit's identifier")
        ) -> json:
            """
            Get circuit information:
                id, str
                full_name, str
                type, str
                place_name, str
                latitude, float
                length, float
                turns, int
                total_races_held, int
                name, str
                previous_names, str
                direction, str
                country_id, str
                longitude, float
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{circuit_id}")
            return result

        @mcp.tool(name="get_circuit_chronology_by_id")
        async def get_circuit_chronology_by_id(
            circuit_id: str = Field(title="circuit_id", description="Circuit's identifier")
        ) -> json:
            """
            Get circuit's F1 chronology list F1 grand prix race in specific circuit:
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/{circuit_id}/chronology")
            return result

        @mcp.tool(name="get_circuit_by_id_and_season")
        async def get_circuit_by_season(
            circuit_id: str = Field(title="circuit_id", description="Circuit's identifier"),
            year: int = Field(title="year", description="Year of the season")
        ) -> json:
            """
            Get circuit's F1 chronology list F1 grand prix race in specific circuit:
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
            result = launch_request_f1db(f"{cls.BASE_PATH}/{circuit_id}/{year}")
            return result