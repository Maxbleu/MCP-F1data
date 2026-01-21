import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class ConstructorTools(BaseTools):

    BASE_PATH = "/constructors"

    @staticmethod
    def get_constructor_by_id(constructor_id: str) -> json:
        """
        Get constructor object by constructor_id.

        :param constructor_id: id of the constructor, str

        :return: json with the constructor object information
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}")
        return result

    @staticmethod
    def search_constructor(constructor: str) -> json:
        """
        Search constructor by name input user.

        :param constructor: name of the constructor, str

        :return: json with the constructor's F1 grand prix race information
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/search",data={"constructor":constructor})
        return result

    @staticmethod
    def get_constructor_chronology(constructor_id: str) -> json:
        """
        Get constructor's F1 chronology list F1 history of specific constructor.

        :param constructor_id: id of the constructor, str

        :return: json with the constructor's F1 grand prix race information
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}/chronology")
        return result

    @staticmethod
    def get_constructor_drivers(constructor_id: str) -> json:
        """
        Get constructor's F1 drivers list F1 history of specific constructor.

        :param constructor_id: id of the constructor, str

        :return: json with the constructor's F1 grand prix race information
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}/drivers")
        return result

    @staticmethod
    def get_constructor_championships(constructor_id: str) -> json:
        """
        Get constructor's F1 championships list F1 history of specific constructor.

        :param constructor_id: id of the constructor, str

        :return: json with the constructor's F1 grand prix race information
        """
        result = launch_request_f1db(f"{ConstructorTools.BASE_PATH}/{constructor_id}/championships")
        return result