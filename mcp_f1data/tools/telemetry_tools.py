import json
from pydantic import Field
from fastmcp import FastMCP
from .base_tools import BaseTools
from ..utils import get_laps, get_specific_lap

class TelemetryTools(BaseTools):
    def __init__(self, mcp_instance: FastMCP):
        super().__init__(mcp_instance=mcp_instance)

    async def get_fastest_lap(
        type_session: str = Field(description="Type of session in general terms: official or pretest (pre-session test)"),
        year: int = Field(description="The year of the season when the session was held"),
        round: int = Field(description="The round number of the championship, for example 1 for the first Grand Prix."),
        session: str = Field(description="The exact name of the session within the event, such as 'FP1', 'FP2', 'Q', 'R', or 'Sprint'."),
        driver: str = Field(description="The abbreviation of the driver's name. If you don't have a specific driver in mind, you can leave this blank to get the fastest lap for all drivers"),
    ) -> json:
        """Get the fastest laps for a driver in a session. In case no driver is specified, it will return the fastest laps for all drivers"""

        laps = get_laps(type_session, year, round, session, driver)
        lap = get_specific_lap(
                laps,
                get_general_fastest_lap = False if driver else True,
                get_personal_fastest_lap= True if driver else False
            )
        return lap.to_json()

    async def get_top_speed(
        type_session: str = Field(description="Type of session in general terms: official or pretest (pre-session test)"),
        year: int = Field(description="The year of the season when the session was held"),
        round: int = Field(description="The round number of the championship, for example 1 for the first Grand Prix."),
        session: str = Field(description="The exact name of the session within the event, such as 'FP1', 'FP2', 'Q', 'R', or 'Sprint'."),
        driver: str = Field(description="The abbreviation of the driver's name. If you don't have a specific driver in mind, you can leave this blank to get the fastest lap for all drivers"),
    ) -> int:
        """Get the top speed for a driver in a session. In case no driver is specified, it will return the highest top speed for all drivers"""

        laps = get_laps(type_session, year, round, session, driver)
        max_speed = int(laps["SpeedST"].max())
        return max_speed

    async def get_deleted_laps(
        type_session: str = Field(description="Type of session in general terms: official or pretest (pre-session test)"),
        year: int = Field(description="The year of the season when the session was held"),
        round: int = Field(description="The round number of the championship, for example 1 for the first Grand Prix."),
        session: str = Field(description="The exact name of the session within the event 'R'"),
        driver: str = Field(description="The abbreviation of the driver's name."),
    ) -> json:
        """Get laps where the driver was in the pit box."""

        laps = get_laps(type_session, year, round, session, driver)
        deleted_laps = laps[laps["Deleted"] == True][["Time","Driver","LapNumber","Deleted","DeletedReason"]]
        return deleted_laps.to_json()
