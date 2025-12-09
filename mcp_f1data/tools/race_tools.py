import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class RaceTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/races"

    @staticmethod
    def get_free_practice_1_by_id(race_id: int) -> json:
        """Get a driver's list result of free practice 1 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_1")

    @staticmethod
    def get_free_practice_1_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of free practice 1 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_1/{driver_id}")

    @staticmethod
    def get_free_practice_2_by_id(race_id: int) -> json:
        """Get a driver's list result of free practice 2 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_2")

    @staticmethod
    def get_free_practice_2_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of free practice 2 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_2/{driver_id}")

    @staticmethod
    def get_free_practice_3_by_id(race_id: int) -> json:
        """Get a driver's list result of free practice 3 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_3")

    @staticmethod
    def get_free_practice_3_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of free practice 3 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_3/{driver_id}")

    @staticmethod
    def get_free_practice_4_by_id(race_id: int) -> json:
        """Get a driver's list result of free practice 4 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_4")

    @staticmethod
    def get_free_practice_4_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of free practice 4 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/practice_4/{driver_id}")

    @staticmethod
    def get_qualy_1_by_id(race_id: int) -> json:
        """Get a driver's list result of qualy 1 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_1")

    @staticmethod
    def get_qualy_1_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of qualy 1 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_1/{driver_id}")

    @staticmethod
    def get_qualy_2_by_id(race_id: int) -> json:
        """Get a driver's list result of qualy 2 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_2")

    @staticmethod
    def get_qualy_2_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of qualy 2 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_2/{driver_id}")

    @staticmethod
    def get_qualy_3_by_id(race_id: int) -> json:
        """Get a driver's list result of qualy 3 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_3")

    @staticmethod
    def get_qualy_3_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of qualy 3 of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy_3/{driver_id}")

    @staticmethod
    def get_pre_qualy_result_by_id(race_id: int) -> json:
        """Get a driver's list pre result of qualy of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy/pre_result")

    @staticmethod
    def get_pre_qualy_result_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver pre result of qualy of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/qualy/pre_result/{driver_id}")

    @staticmethod
    def get_starting_grid_by_id(race_id: int) -> json:
        """Get a driver's list starting grid of the race of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/grid")

    @staticmethod
    def get_starting_grid_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver starting grid of the race of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/grid/{driver_id}")

    @staticmethod
    def get_driver_of_the_day_by_id(race_id: int) -> json:
        """Get driver of the day of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/driver_of_the_day")

    @staticmethod
    def get_fastest_lap_by_id(race_id: int) -> json:
        """Get the driver with the fastest lap of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/fastest_lap")

    @staticmethod
    def get_fastest_lap_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver fastest lap of the race of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/fastest_lap/{driver_id}")

    @staticmethod
    def get_race_result_by_id(race_id: int) -> json:
        """Get race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race")

    @staticmethod
    def get_race_result_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get driver race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/race/{driver_id}")

    @staticmethod
    def get_sprint_qualy_by_id(race_id: int) -> json:
        """Get a driver's list result of sprint qualy of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint_qualy")

    @staticmethod
    def get_sprint_qualy_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver result of sprint qualy of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint_qualy/{driver_id}")

    @staticmethod
    def get_sprint_starting_grid_by_id(race_id: int) -> json:
        """Get a driver's list sprint starting grid of the race of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint/grid")

    @staticmethod
    def get_sprint_starting_grid_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get a driver sprint starting grid of the race of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint/grid/{driver_id}")

    @staticmethod
    def get_sprint_race_result_by_id(race_id: int) -> json:
        """Get sprint race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint")

    @staticmethod
    def get_sprint_race_result_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get driver sprint race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/sprint/{driver_id}")

    @staticmethod
    def get_warming_up_by_id(race_id: int) -> json:
        """Get driver sprint race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/warming_up")

    @staticmethod
    def get_warming_up_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get driver sprint race result of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/warming_up/{driver_id}")

    @staticmethod
    def get_pit_stop_by_id(race_id: int) -> json:
        """Get every pit stop of specific race in a list"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/pit_stop")

    @staticmethod
    def get_pit_stop_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get every pit stop of one driver of specific race in a list"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/pit_stop/{driver_id}")

    @staticmethod
    def get_gp_driver_summary_by_id_and_driver_id(race_id: int, driver_id: str) -> json:
        """Get driver grand prix summary of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/gp_wekend_summary/{driver_id}")

    @staticmethod
    def get_driver_standing_by_id(race_id: int) -> json:
        """Get driver standing list of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/driver_standing")

    @staticmethod
    def get_driver_standing_by_id_and_driver(race_id: int, driver_id: str) -> json:
        """Get driver standing of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/driver_standing/{driver_id}")

    @staticmethod
    def get_constructor_standing_by_id(race_id: int) -> json:
        """Get constructor standing list of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/constructor_standing")

    @staticmethod
    def get_constructor_standing_by_id_and_constructor(race_id: int, constructor_id: str) -> json:
        """Get constructor standing of specific race"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{race_id}/constructor_standing/{constructor_id}")

    @staticmethod
    def get_race_by_year_and_round(year: int, round: int) -> json:
        """Get a specific race by year and specific round"""
        return launch_request_f1db(f"{RaceTools.BASE_PATH}/{year}/{round}")