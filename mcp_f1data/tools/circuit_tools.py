import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class CircuitTools(BaseTools):
    BASE_PATH = "/circuits"

    @staticmethod
    def get_circuit_by_id(circuit_id: str) -> json:
        """
        Get circuit object by circuit_id.

        :param circuit_id: id of the circuit, str

        :return: json with the circuit object information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}")
        return result

    @staticmethod
    def search_circuit(circuit: str) -> json:
        """
        Search circuit by name input user.

        :param circuit: name of the circuit, str

        :return: json with the circuit's F1 grand prix race information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/search",data={"circuit":circuit})
        return result

    @staticmethod
    def get_circuit_chronology_by_id(circuit_id: str) -> json:
        """
        Get circuit's F1 chronology list F1 grand prix 
        race in specific circuit.

        :param circuit_id: id of the circuit, str

        :return: json with the circuit's F1 grand prix race information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/chronology")
        return result

    @staticmethod
    def get_circuit_by_season(circuit_id: str, year: int) -> json:
        """
        Get circuit's F1 grand prix race in specific circuit.

        :param circuit_id: id of the circuit, str
        :param year: year of the season, int

        :return: json with the circuit's F1 grand prix race information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/{year}")
        return result

    @staticmethod
    def get_circuit_drivers_championship_decider_by_id(circuit_id: str) -> json:
        """
        Get from a specific circuit times when a driver
        get the drivers championship

        :param circuit_id: id of the circuit, str

        :return: json with the drivers championship decider information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/championship_decider/drivers")
        return result

    @staticmethod
    def get_circuit_constructors_championship_decider_by_id(circuit_id: str) -> json:
        """
        Get times when a constructor get the constructors 
        championship in a specific circuit.

        :param circuit_id: id of the circuit, str

        :return: json with the constructors championship decider information
        """
        result = launch_request_f1db(f"{CircuitTools.BASE_PATH}/{circuit_id}/championship_decider/constructors")
        return result