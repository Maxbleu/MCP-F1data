import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class CircuitTools(BaseTools):
    BASE_PATH = "/circuits"

    @staticmethod
    def search_circuit(circuit: str) -> json:
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

        IMPORTANT
        In the parameter indicate only 
        the circuit's name e.g:
            - I want to know about Imola's circuit, Enzo Dino Ferrari -> Enzo Dino Ferrari
            - Avus -> Avus
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/search",data={"circuit":circuit})
        return result

    @staticmethod
    def get_circuit_chronology_by_id(circuit_id: str) -> json:
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
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/chronology")
        return result

    @staticmethod
    def get_circuit_by_season(circuit_id: str, year: int) -> json:
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
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/{year}")
        return result