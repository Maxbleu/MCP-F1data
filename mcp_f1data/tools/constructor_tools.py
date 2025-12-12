import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class ConstructorTools(BaseTools):

    BASE_PATH = "/constructors"

    @staticmethod
    def search_constructor(constructor: str) -> json:
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

            IMPORTANT
            In the parameter indicate only 
            the constructor's name e.g:
                - I want to know about Mercedes -> Mercedes
                - Behra Porsche -> Behra Porsche
                - Matra -> Matra
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/search",data={"constructor":constructor})
        return result

    @staticmethod
    def get_constructor_chronology(constructor_id: str) -> json:
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
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}/chronology")
        return result

    @staticmethod
    def get_constructor_drivers(constructor_id: str) -> json:
        """
        Get constructor's F1 drivers list F1 history of specific constructor:
            engine_manufacturer_id, str
            constructor_id, str
            year, int
            rounds", str
            entrant, obj
            driver, obj
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}/drivers")
        return result