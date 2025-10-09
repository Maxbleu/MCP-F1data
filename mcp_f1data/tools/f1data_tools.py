import json, requests, os
from pydantic import Field
from fastmcp import FastMCP
import fastf1.plotting as f1_plotting
from ..utils.fastf1_utils import get_laps, get_specific_lap, get_session

def register_f1data_tools(mcp:FastMCP):
    """Register all F1 analysis tools with the MCP server"""

    @mcp.tool(name="get_driver_by_id")
    async def get_driver_by_id(
        driver_id: str = Field(description="Driver's identifier")
    ) -> json:
        """
        Get driver information:
            id, str
            name, str
            first_name, str
            last_name, str
            full_name, str
            abbreviation, str
            permanent_number, int
            gender, str
            date_of_birth, date
            date_of_death, date
            place_of_birth, str
            country_of_birth_country_id, str
            nationality_country_id, str
            second_nationality_country_id, str
            best_championship_position, int
            best_starting_grid_position, int
            best_race_result, int
            total_championship_wins, int
            total_race_entries, int
            total_race_starts, int
            total_race_wins, int
            total_race_laps, int
            total_podiums, int
            total_points, float
            total_championship_points, float
            total_pole_positions, int
            total_fastest_laps, int
            total_driver_of_the_day, int
            total_grand_slams, int
        """

        headers = {"Authorization": f"Bearer {os.getenv("JWT_TOKEN")}"}
        response = requests.get(url=f"https://apif1db-production.up.railway.app/api/drivers/{driver_id}",headers=headers)
        if response.status_code == 200:
            json = response.json()
            return json

    @mcp.tool(name="get_driver_family_relationship")
    async def get_driver_family_relationship(
        driver_id: str = Field(description="Driver's identifier")
    ) -> json:
        """
        Get driver's F1 familiries of specific driver:
            driver_id, str
            position_display_order, int
            other_driver_id, str
            type, str
        """

        headers = {"Authorization": f"Bearer {os.getenv("JWT_TOKEN")}"}
        response = requests.get(url=f"https://apif1db-production.up.railway.app/api/drivers/{driver_id}/family_relationship",headers=headers)
        if response.status_code == 200:
            json = response.json()
            return json

    @mcp.tool(name="get_fastest_lap")
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

    @mcp.tool(name="get_top_speed")
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

    @mcp.tool(name="get_deleted_laps")
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