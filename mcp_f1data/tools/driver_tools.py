import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import launch_request_f1db

class DriverTools(BaseTools):
    def __init__(self, mcp: FastMCP):
        super().__init__(mcp=mcp)

    BASE_PATH = "/drivers"

    @staticmethod
    def search_driver(driver: str) -> json:
        """
        Get driver profole of specific driver
        """
        result = launch_request_f1db(f"{DriverTools.BASE_PATH}/search",data={"driver":driver})
        return result

    @staticmethod
    def get_driver_family_relationship_by_id(driver_id: str) -> json:
        """
        Get driver's F1 families list of specific driver
        """
        result = launch_request_f1db(f"{DriverTools.BASE_PATH}/{driver_id}/family_relationship")
        return result

    @staticmethod
    def get_driver_career_by_id(driver_id: str) -> json:
        """
        Get driver's F1 career list of specific constructors, which drives in the past
        """
        result = launch_request_f1db(f"{DriverTools.BASE_PATH}/{driver_id}/career")
        return result