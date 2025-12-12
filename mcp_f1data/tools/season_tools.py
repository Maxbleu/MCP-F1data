import json
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class SeasonTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/seasons"

    @staticmethod
    def get_season_grand_prix_by_year(year: int) -> json:
        """
        Get a list of every grand prix of the season:
            id, str
            year, int
            round, int
            grand_prix_id, str
            circuit_id, str
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/grand_prix")
        return result

    @staticmethod
    def get_grand_prix_by_race_id(year: int, race_id: int) -> json:
        """
        Get a grand prix in specific season:
            id, str
            year, int
            round, int
            grand_prix_id, str
            circuit_id, str
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/grand_prix/{race_id}")
        return result

    @staticmethod
    def get_grand_prix_by_year_and_round(year: int, round: int) -> json:
        """
        Get a grand prix in specific season:
            id, str
            year, int
            round, int
            grand_prix_id, str
            circuit_id, str
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/{round}")
        return result

    @staticmethod
    def get_constructor_by_year(year: int) -> json:
        """
        Get list of every entrant constructor of the season:
            engine_manufacturer_id, str
            year, int
            constructor, obj
            entrant, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors")
        return result

    @staticmethod
    def get_constructor_by_year_and_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get a specific constructor of the season:
            engine_manufacturer_id, str
            year, int
            constructor, obj
            entrant, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors/{constructor_id}")
        return result

    @staticmethod
    def get_constructor_drivers_by_year_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get constructor's F1 drivers list about one constructor in specific season:
            engine_manufacturer_id, str
            constructor_id, str
            year, int
            rounds", str
            entrant, obj
            driver, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors/{constructor_id}/drivers")
        return result

    @staticmethod
    def get_driver_by_year(year: int) -> json:
        """
        Get list of every entrant drivers of the season:
            constructor_id, str
            engine_manufacturer_id, str
            year, int
            rounds, str
            entrant, obk
            driver, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/drivers")
        return result

    @staticmethod
    def get_driver_by_year_and_driver_id(year: int, driver_id: str) -> json:
        """
        Get a specific driver of the season:
            constructor_id, str
            engine_manufacturer_id, str
            year, int
            rounds, str
            entrant, obk
            driver, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/drivers/{driver_id}")
        return result

    @staticmethod
    def get_tyres_stats_by_year(year: int) -> json:
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
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/tyres/stats")
        return result

    @staticmethod
    def get_engines_stats_by_year(year: int) -> json:
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
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/engines/stats")
        return result

    @staticmethod
    def get_chassis_by_year(year: int) -> json:
        """
        Get a list of every constructor's chassis of the season:
            year, int
            engine_manufacturer_id, str
            entrant, obj
            chassis, obj
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/chassis")
        return result

    @staticmethod
    def get_driver_standing_by_year(year: int) -> json:
        """
        Get a list of drivers standing of the season:
            driver_id, str
            year, int
            position_display_order, int
            position_number, int
            position_text, str
            points, float
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standing/drivers")
        return result

    @staticmethod
    def get_driver_standing_specific_by_year_and_driver_id(year: int, driver_id: str) -> json:
        """
        Get a driver standing in specific season:
            driver_id, str
            year, int
            position_display_order, int
            position_number, int
            position_text, str
            points, float
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standing/drivers/{driver_id}")
        return result

    @staticmethod
    def get_constructor_standing_by_year(year: int) -> json:
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
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standing/constructors")
        return result

    @staticmethod
    def get_constructor_standing_specific_by_year_and_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get a constructor standing in specific season:
            constructor_id, str
            year, int
            position_display_order, int
            position_number, int
            position_text, str
            points, float
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standing/constructors/{constructor_id}")
        return result