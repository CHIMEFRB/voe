"""format a VOE for a TNS submission."""

from typing import Any, Dict

import requests
from pydantic import Field

from frbvoe.models.voe import VOEvent


class TNS(VOEvent):
    """Represents a TNS (Transient Name Server) object.

    Attributes:
        tns_api_key (str): API key for the TNS.
        tns_marker (str): Marker for the TNS.
        tns_id (int): ID for the TNS.
    """

    tns_api_key: str = Field(
        ..., description="API key for the TNS", example="1234567890"
    )
    tns_marker: str = Field(..., description="Marker for the TNS", example="FRB")
    tns_id: int = Field(..., description="ID for the TNS", example="1234567890")

    def submit(
        self, voevent: Dict[str, Any], api_key, tns_id, bot_name, tns_marker, url
    ):
        """Submits a VOEvent to the TNS API.

        Args:
            voevent (Dict[str, Any]): The VOEvent data to be submitted.
            api_key: The API key for authentication.
            tns_id: The TNS ID.
            bot_name: The name of the bot submitting the VOEvent.
            tns_marker: The TNS marker.
            url: The URL of the TNS API.

        Returns:
            The response from the TNS API.

        Raises:
            requests.HTTPError: If the request to the TNS API fails.
        """
        headers = {"User-Agent": tns_marker}
        json_data = {"api_key": api_key, "data": voevent}
        response = requests.post(url, headers=headers, data=json_data)
        response.raise_for_status()
        return response


# TODO: Functionality
# from frbvoe.models.voe import VOEvent

# voe = VOEvent(...)
# tns = TNS(**voe.payload)
