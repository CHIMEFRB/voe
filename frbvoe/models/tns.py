"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging

# import requests
from pydantic import Field

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


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

    @property
    def submit(voevent: Dict[str, Any]):
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
        # headers = {"User-Agent": tns_marker}
        # json_data = {"api_key": api_key, "data": voevent}
        log.info("Sending VOE payload to TNS.")
        # response = requests.post(url, headers=headers, data=json_data)
        # response.raise_for_status()
        # return response
        pass
