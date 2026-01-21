import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class ManufacturerTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/manufacturers"

    @staticmethod
    def search_tyre_manufacturer(tyre_manufacturer: str) -> json:
        """
        Search a scpecific tyre manufacturer along of F1 history.

        :param tyre_manufacturer: name of the tyre manufacturer, str

        :return: json with the tyre manufacturer's information
        """
        result = launch_request_f1db(f"{ManufacturerTools.BASE_PATH}/tyres/search",data={"tyre_manufacturer":tyre_manufacturer})
        return result

    @staticmethod
    def search_engine_manufacturer(engine_manufacturer: str) -> json:
        """
        Search a scpecific engine manufacturer along of F1 history.

        :param engine_manufacturer: name of the engine manufacturer, str

        :return: json with the engine manufacturer's information
        """
        result = launch_request_f1db(f"{ManufacturerTools.BASE_PATH}/engines/search", data={"engine_manufacturer":engine_manufacturer})
        return result