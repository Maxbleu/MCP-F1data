import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class GrandPrixTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/grand_prix"

    @staticmethod
    def get_grand_prix_by_id(grand_prix_id: str) -> json:
        """
        Get grand prix historical information

        :param grand_prix_id: id of the grand prix, str

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/{grand_prix_id}")
        return result

    @staticmethod
    def search_grand_prix(grand_prix: str) -> json:
        """
        Search grand prix by name input user

        :param grand_prix: name of the grand prix, str

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/search",data={"grand_prix":grand_prix})
        return result

    @staticmethod
    def get_grand_prix_by_id_and_year(grand_prix_id: str, year: int) -> json:
        """
        Get grand prix of especific season

        :param grand_prix_id: id of the grand prix, str
        :param year: year of the grand prix, int

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/{grand_prix_id}/{year}")
        return result

    @staticmethod
    def get_grand_prix_chronology_by_id(grand_prix_id: str) -> json:
        """
        Get a list of specific F1 Grands Prix held at circuits at long of F1 history

        :param grand_prix_id: id of the grand prix, str

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/{grand_prix_id}/chronology")
        return result

    @staticmethod
    def get_grand_prix_drivers_championship_decider_by_id(grand_prix_id: str) -> json:
        """
        Get a list of F1 Grands Prix held at different 
        circuits that decided the Constructors' Championship

        :param grand_prix_id: id of the grand prix, str

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/{grand_prix_id}/championship_decider/drivers")
        return result

    @staticmethod
    def get_grand_prix_constructors_championship_decider_by_id(grand_prix_id: str) -> json:
        """
        Get a list of F1 Grands Prix held at different circuits 
        that decided the Constructors' Championship

        :param grand_prix_id: id of the grand prix, str

        :return: json with the grand prix's F1 grand prix race information
        """
        result = launch_request_f1db(f"{GrandPrixTools.BASE_PATH}/{grand_prix_id}/championship_decider/constructors")
        return result