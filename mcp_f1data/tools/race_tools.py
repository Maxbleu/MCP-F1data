import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class RaceTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/races"

    @classmethod
    def __register_mcp_tools__(cls, mcp: FastMCP) -> None:
        """Register all race tools with MCP"""

        #   FP1
        @mcp.tool(name="get_free_practice_1_by_id")
        async def get_free_practice_1_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of free practice 1 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_1")
            return result

        @mcp.tool(name="get_free_practice_1_by_id_and_driver_id")
        async def get_free_practice_1_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of free practice 1 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_1/{driver_id}")
            return result

        #   FP2
        @mcp.tool(name="get_free_practice_2_by_id")
        async def get_free_practice_2_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of free practice 2 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_2")
            return result

        @mcp.tool(name="get_free_practice_2_by_id_and_driver_id")
        async def get_free_practice_2_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of free practice 2 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_2/{driver_id}")
            return result

        #   FP3
        @mcp.tool(name="get_free_practice_3_by_id")
        async def get_free_practice_3_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of free practice 3 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_3")
            return result

        @mcp.tool(name="get_free_practice_3_by_id_and_driver_id")
        async def get_free_practice_3_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of free practice 3 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_3/{driver_id}")
            return result

        #   FP4
        @mcp.tool(name="get_free_practice_4_by_id")
        async def get_free_practice_4_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of free practice 4 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_4")
            return result

        @mcp.tool(name="get_free_practice_4_by_id_and_driver_id")
        async def get_free_practice_4_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of free practice 4 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/practice_4/{driver_id}")
            return result

        #   Q1
        @mcp.tool(name="get_qualy_1_by_id")
        async def get_qualy_1_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of qualy 1 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_1")
            return result

        @mcp.tool(name="get_qualy_1_by_id_and_driver_id")
        async def get_qualy_1_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of qualy 1 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_1/{driver_id}")
            return result

        #   Q2
        @mcp.tool(name="get_qualy_2_by_id")
        async def get_qualy_2_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of qualy 2 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_2")
            return result

        @mcp.tool(name="get_qualy_2_by_id_and_driver_id")
        async def get_qualy_2_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of qualy 2 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_2/{driver_id}")
            return result

        #   Q3
        @mcp.tool(name="get_qualy_3_by_id")
        async def get_qualy_3_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of qualy 3 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
                q1, str
                q1_millis, int
                q2, str
                q2_millis, int
                q3, str
                q3_millis, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_3")
            return result

        @mcp.tool(name="get_qualy_3_by_id_and_driver_id")
        async def get_qualy_3_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of qualy 3 of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
                q1, str
                q1_millis, int
                q2, str
                q2_millis, int
                q3, str
                q3_millis, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy_3/{driver_id}")
            return result

        #   PRE QUALY RESULT
        @mcp.tool(name="get_pre_qualy_result_by_id")
        async def get_pre_qualy_result_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list pre result of qualy of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy/pre_result")
            return result

        @mcp.tool(name="get_pre_qualy_result_by_id_and_driver_id")
        async def get_pre_qualy_result_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver pre result of qualy of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/qualy/pre_result/{driver_id}")
            return result

        #   GRID
        @mcp.tool(name="get_starting_grid_by_id")
        async def get_starting_grid_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list starting grid of the race of specific race:
                driver_number, str
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                qualification_position_text, str
                grid_penalty_positions, int
                time_millis, int
                race_id, int
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                qualification_position_number, int
                grid_penalty, str
                time, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/grid")
            return result

        @mcp.tool(name="get_starting_grid_by_id_and_driver_id")
        async def get_starting_grid_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver starting grid of the race of specific race:
                driver_number, str
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                qualification_position_text, str
                grid_penalty_positions, int
                time_millis, int
                race_id, int
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                qualification_position_number, int
                grid_penalty, str
                time, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/grid/{driver_id}")
            return result

        #   DRIVER OF THE DAY
        @mcp.tool(name="get_driver_of_the_day_by_id")
        async def get_driver_of_the_day_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get driver of the day of specific race:
                position_display_order, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                percentage, float
                position_number, int
                driver_number, str
                race_id, int
                constructor_id, str
                tyre_manufacturer_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/driver_of_the_day")
            return result

        #   FASTEST LAP
        @mcp.tool(name="get_fastest_lap_by_id")
        async def get_fastest_lap_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get the driver with the fastest lap of specific race:
                position_text, str
                position_number, int
                driver_id, str
                engine_manufacturer_id, str
                lap, int
                time_millis, int
                gap_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                time, str
                gap, str
                interval int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/fastest_lap")
            return result

        @mcp.tool(name="get_fastest_lap_by_id_and_driver_id")
        async def get_fastest_lap_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver starting grid of the race of specific race:
                position_text, str
                position_number, int
                driver_id, str
                engine_manufacturer_id, str
                lap, int
                time_millis, int
                gap_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                time, str
                gap, str
                interval int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/fastest_lap/{driver_id}")
            return result

        #   RACE
        @mcp.tool(name="get_race_result_by_id")
        async def get_race_result_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get race result of specific race:
                tyre_manufacturer_id, str
                qualification_position_number, int
                grand_slam, bool
                position_display_order, int
                shared_car, bool
                gap_millis, int
                qualification_position_text, str
                position_text, str
                race_id, int
                position_number, int
                laps, int
                gap, str
                gap_laps, int
                grid_position_number, int
                time, str
                interval, str
                grid_position_text, str
                driver_number, str
                time_millis, int
                interval_millis, int
                positions_gained, str
                driver_id, str
                time_penalty, str
                reason_retired, str
                pit_stops, int
                constructor_id, str
                time_penalty_millis, int
                points, float
                fastest_lap, bool
                engine_manufacturer_id, str
                pole_position, bool
                driver_of_the_day, bool
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race")
            return result

        @mcp.tool(name="get_race_result_by_id_and_driver_id")
        async def get_race_result_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get driver race result of specific race:
                tyre_manufacturer_id, str
                qualification_position_number, int
                grand_slam, bool
                position_display_order, int
                shared_car, bool
                gap_millis, int
                qualification_position_text, str
                position_text, str
                race_id, int
                position_number, int
                laps, int
                gap, str
                gap_laps, int
                grid_position_number, int
                time, str
                interval, str
                grid_position_text, str
                driver_number, str
                time_millis, int
                interval_millis, int
                positions_gained, str
                driver_id, str
                time_penalty, str
                reason_retired, str
                pit_stops, int
                constructor_id, str
                time_penalty_millis, int
                points, float
                fastest_lap, bool
                engine_manufacturer_id, str
                pole_position, bool
                driver_of_the_day, bool
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/race/{driver_id}")
            return result

        #   SPRINT QUALY
        @mcp.tool(name="get_sprint_qualy_by_id")
        async def get_sprint_qualy_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list result of sprint qualy of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
                q1, str
                q1_millis, int
                q2, str
                q2_millis, int
                q3, str
                q3_millis, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint_qualy")
            return result

        @mcp.tool(name="get_sprint_qualy_by_id_and_driver_id")
        async def get_sprint_qualy_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver result of sprint qualy of specific race:
                race_id, int
                driver_number, str
                constructor_id, str
                tyre_manufacturer_id, str
                time_millis, int
                gap_millis, int
                interval_millis, int
                position_display_order, iont
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                time, str
                gap, str
                interval, str
                laps, int
                q1, str
                q1_millis, int
                q2, str
                q2_millis, int
                q3, str
                q3_millis, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint_qualy/{driver_id}")
            return result

        #   SPRINT GRID
        @mcp.tool(name="get_sprint_starting_grid_by_id")
        async def get_sprint_starting_grid_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get a driver's list sprint starting grid of the race of specific race:
                driver_number, str
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                qualification_position_text, str
                grid_penalty_positions, int
                time_millis, int
                race_id, int
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                qualification_position_number, int
                grid_penalty, str
                time, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint/grid")
            return result

        @mcp.tool(name="get_sprint_starting_grid_by_id_and_driver_id")
        async def get_sprint_starting_grid_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get a driver sprint starting grid of the race of specific race:
                driver_number, str
                position_display_order, int
                constructor_id, str
                tyre_manufacturer_id, str
                qualification_position_text, str
                grid_penalty_positions, int
                time_millis, int
                race_id, int
                position_number, int
                position_text, str
                driver_id, str
                engine_manufacturer_id, str
                qualification_position_number, int
                grid_penalty, str
                time, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint/grid/{driver_id}")
            return result

        #   SPRINT
        @mcp.tool(name="get_sprint_race_result_by_id")
        async def get_sprint_race_result_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get sprint race result of specific race:
                position_number, int
                laps, int
                grid_position_text, str
                position_display_order, int
                time, str
                interval, str
                positions_gained, str
                position_text, str
                time_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                time_penalty, str
                reason_retired, str
                driver_id, str
                time_penalty_millis, int
                points, float
                constructor_id, str
                gap, str
                qualification_position_number, int
                engine_manufacturer_id, str
                gap_millis, int
                qualification_position_text, str
                tyre_manufacturer_id, str
                gap_laps, int
                grid_position_number, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint")
            return result

        @mcp.tool(name="get_sprint_race_result_by_id_and_driver_id")
        async def get_sprint_race_result_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get driver sprint race result of specific race:
                position_number, int
                laps, int
                grid_position_text, str
                position_display_order, int
                time, str
                interval, str
                positions_gained, str
                position_text, str
                time_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                time_penalty, str
                reason_retired, str
                driver_id, str
                time_penalty_millis, int
                points, float
                constructor_id, str
                gap, str
                qualification_position_number, int
                engine_manufacturer_id, str
                gap_millis, int
                qualification_position_text, str
                tyre_manufacturer_id, str
                gap_laps, int
                grid_position_number, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/sprint/{driver_id}")
            return result

        #   WARMING
        @mcp.tool(name="get_warming_up_by_id")
        async def get_warming_up_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get driver sprint race result of specific race:
                position_number, int
                laps, int
                position_display_order, int
                time, str
                interval, str
                position_text, str
                time_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                driver_id, str
                constructor_id, str
                gap, str
                engine_manufacturer_id, str
                gap_millis, int
                tyre_manufacturer_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/warming_up")
            return result

        @mcp.tool(name="get_warming_up_by_id_and_driver_id")
        async def get_warming_up_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get driver sprint race result of specific race:
                position_number, int
                laps, int
                position_display_order, int
                time, str
                interval, str
                position_text, str
                time_millis, int
                interval_millis, int
                driver_number, str
                race_id, int
                driver_id, str
                constructor_id, str
                gap, str
                engine_manufacturer_id, str
                gap_millis, int
                tyre_manufacturer_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/warming_up/{driver_id}")
            return result

        #   PIT STOP
        @mcp.tool(name="get_pit_stop_by_id")
        async def get_pit_stop_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get every pit stop of specific race in a list:
                position_number, int
                position_display_order, int
                time, str
                position_text, str
                time_millis, int
                driver_number, str
                race_id, int
                driver_id, str
                constructor_id, str
                engine_manufacturer_id, str
                tyre_manufacturer_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/warming_up")
            return result

        @mcp.tool(name="get_pit_stop_by_id_and_driver_id")
        async def get_pit_stop_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get every pit stop of one driver of specific race in a list:
                position_number, int
                position_display_order, int
                time, str
                position_text, str
                time_millis, int
                driver_number, str
                race_id, int
                driver_id, str
                constructor_id, str
                engine_manufacturer_id, str
                tyre_manufacturer_id, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/warming_up/{driver_id}")
            return result

        #   RACE DATA
        @mcp.tool(name="get_gp_driver_summary_by_id_and_driver_id")
        async def get_gp_driver_summary_by_id_and_driver_id(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get driver grand prix summary of specific race:
                race_id, int
                type, str
                position_display_order, int
                position_number, int
                position_text, str
                driver_number, str
                driver_id, str
                constructor_id, str
                engine_manufacturer_id, str
                tyre_manufacturer_id, str
                practice_time, str
                practice_time_millis, int
                practice_gap, str
                practice_gap_millis, int
                practice_interval, str
                practice_interval_millis, int
                practice_laps, int
                qualifying_time, str
                qualifying_time_millis, int
                qualifying_q1, str
                qualifying_q1_millis, int
                qualifying_q2, str
                qualifying_q2_millis, int
                qualifying_q3, str
                qualifying_q3_millis, int
                qualifying_gap, str
                qualifying_gap_millis, int
                qualifying_interval, str
                qualifying_interval_millis, int
                qualifying_laps, int
                starting_grid_position_qualification_position_number, int
                starting_grid_position_qualification_position_text, str
                starting_grid_position_grid_penalty, str
                starting_grid_position_grid_penalty_positions, int
                starting_grid_position_time, str
                starting_grid_position_time_millis, int
                race_shared_car, bool
                race_laps, int
                race_time, str
                race_time_millis, int
                race_time_penalty, str
                race_time_penalty_millis, int
                race_gap, str
                race_gap_millis, int
                race_gap_laps, int
                race_interval, str
                race_interval_millis, int
                race_reason_retired, str
                race_points, float
                race_pole_position, bool
                race_qualification_position_number, int
                race_qualification_position_text, str
                race_grid_position_number, int
                race_grid_position_text, str
                race_positions_gained, int
                race_pit_stops, int
                race_fastest_lap, bool
                race_driver_of_the_day, bool
                race_grand_slam, bool
                fastest_lap_lap, int
                fastest_lap_time, str
                fastest_lap_time_millis, int
                fastest_lap_gap, str
                fastest_lap_gap_millis, int
                fastest_lap_interval, str
                fastest_lap_interval_millis, int
                pit_stop_stop, int
                pit_stop_lap, int
                pit_stop_time, str
                pit_stop_time_millis, int
                driver_of_the_day_percentage, float
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/gp_wekend_summary/{driver_id}")
            return result

        #   STANDING
        @mcp.tool(name="get_driver_standing_by_id")
        async def get_driver_standing_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get driver standing list of specific race:
                race_id, int
                position_display_order, int
                position_number, int
                position_text, str
                driver_id, str
                points, float
                positions_gained, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/driver_standing")
            return result

        @mcp.tool(name="get_driver_standing_by_id_and_driver")
        async def get_driver_standing_by_id_and_driver(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            driver_id: str = Field(title="driver_id", description="Driver's identifier")
        ) -> json:
            """
            Get driver standing of specific race:
                race_id, int
                position_display_order, int
                position_number, int
                position_text, str
                driver_id, str
                points, float
                positions_gained, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/driver_standing/{driver_id}")
            return result

        @mcp.tool(name="get_constructor_standing_by_id")
        async def get_constructor_standing_by_id(
            race_id: int = Field(title="race_id", description="Race's identifier")
        ) -> json:
            """
            Get constructor standing list of specific race:
                race_id, int
                position_display_order, int
                position_number, int
                position_text, str
                constructor_id, str
                points, float
                positions_gained, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/constructor_standing")
            return result

        @mcp.tool(name="get_constructor_standing_by_id_and_constructor")
        async def get_constructor_standing_by_id_and_constructor(
            race_id: int = Field(title="race_id", description="Race's identifier"),
            constructor_id: str = Field(title="constructor_id", description="Constructor's identifier")
        ) -> json:
            """
            Get constructor standing of specific race:
                race_id, int
                position_display_order, int
                position_number, int
                position_text, str
                constructor_id, str
                points, float
                positions_gained, int
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{race_id}/constructor_standing/{constructor_id}")
            return result

        #   GET RACE
        @mcp.tool(name="get_race_by_year_and_round")
        async def get_race_by_year_and_round(
            year: int = Field(title="year", description="Year of the season"), 
            round: int = Field(title="round", description="Round of the season")
        )  -> json:
            """
            Get a specific race by year and specific round:
                id, int
                year, int
                round, int
                date, date
                time, str
                grand_prix, obj
                official_name, str
                qualifying_format, str
                circuit, obj
                circuit_type, str
                direction, str
                course_length, float
                turns, int
                distance, float
                scheduled_laps, int
                scheduled_distance, float
                drivers_championship_decider, bool
                constructors_championship_decider, bool
                pre_qualifying_date, date
                pre_qualifying_time, str
                free_practice_1_date, date
                free_practice_1_time, str
                free_practice_2_date, date
                free_practice_2_time, str
                free_practice_3_date, date
                free_practice_3_time, str
                free_practice_4_date, date
                free_practice_4_time, str
                qualifying_1_date, date
                qualifying_1_time, str
                qualifying_2_date, date
                qualifying_2_time, str
                qualifying_date, date
                qualifying_time, str
                sprint_qualifying_date, date
                sprint_qualifying_time, str
                sprint_race_date, date
                sprint_race_time, str
                warming_up_date, date
                warming_up_time, str
            """
            result = launch_request_f1db(f"{cls.BASE_PATH}/{year}/{round}")
            return result