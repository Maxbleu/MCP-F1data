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
        Get a list of every grand prix of the season.

        :param year: Season year, int

        :return: json with the grand prix's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/grand_prix")
        return result

    @staticmethod
    def get_grand_prix_by_race_id(year: int, race_id: int) -> json:
        """
        Get a grand prix in specific season.

        :param year: Season year, int
        :param race_id: Grand prix id, int

        :return: json with the grand prix's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/grand_prix/{race_id}")
        return result

    @staticmethod
    def get_grand_prix_by_year_and_round(year: int, round: int) -> json:
        """
        Get a grand prix in specific season.

        :param year: Season year, int
        :param round: Grand prix round, int

        :return: json with the grand prix's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/{round}")
        return result

    @staticmethod
    def get_constructor_by_year(year: int) -> json:
        """
        Get list of every entrant constructor of the season.

        :param year: Season year, int

        :return: json with the constructor's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors")
        return result

    @staticmethod
    def get_constructor_by_year_and_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get a specific constructor of the season.

        :param year: Season year, int
        :param constructor_id: Constructor id, str

        :return: json with the constructor's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors/{constructor_id}")
        return result

    @staticmethod
    def get_constructor_drivers_by_year_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get constructor's F1 drivers list about 
        one constructor in specific season.

        :param year: Season year, int
        :param constructor_id: Constructor id, str

        :return: json with the constructor's drivers information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/constructors/{constructor_id}/drivers")
        return result

    @staticmethod
    def get_driver_by_year(year: int) -> json:
        """
        Get list of every entrant drivers of the season.

        :param year: Season year, int

        :return: json with the driver's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/drivers")
        return result

    @staticmethod
    def get_driver_by_year_and_driver_id(year: int, driver_id: str) -> json:
        """
        Get a specific driver of the season.

        :param year: Season year, int
        :param driver_id: Driver id, str

        :return: json with the driver's information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/drivers/{driver_id}")
        return result

    @staticmethod
    def get_tyres_stats_by_year(year: int) -> json:
        """
        Get a list of every tyre's stats of the season.

        :param year: Season year, int

        :return: json with the tyre's stats information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/tyres")
        return result

    @staticmethod
    def get_engines_stats_by_year(year: int) -> json:
        """
        Get a list of every engine's stats of the season.

        :param year: Season year, int

        :return: json with the engine's stats information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/engines")
        return result

    @staticmethod
    def get_chassis_by_year(year: int) -> json:
        """
        Get a list of every constructor's chassis of the season.

        :param year: Season year, int

        :return: json with the constructor's chassis information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/chassis")
        return result

    @staticmethod
    def get_driver_standing_by_year(year: int) -> json:
        """
        Get a list of drivers standing of the season.

        :param year: Season year, int

        :return: json with the driver's standing information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standings/drivers")
        return result

    @staticmethod
    def get_driver_standing_specific_by_year_and_driver_id(year: int, driver_id: str) -> json:
        """
        Get a driver standing in specific season.

        :param year: Season year, int
        :param driver_id: Driver id, str

        :return: json with the driver's standing information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standings/drivers/{driver_id}")
        return result

    @staticmethod
    def get_constructor_standing_by_year(year: int) -> json:
        """
        Get a list of every constructor of the season.

        :param year: Season year, int

        :return: json with the constructor's standing information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standings/constructors")
        return result

    @staticmethod
    def get_constructor_standing_specific_by_year_and_constructor_id(year: int, constructor_id: str) -> json:
        """
        Get a constructor standing in specific season.

        :param year: Season year, int
        :param constructor_id: Constructor id, str

        :return: json with the constructor's standing information
        """
        result = launch_request_f1db(f"{SeasonTools.BASE_PATH}/{year}/standings/constructors/{constructor_id}")
        return result