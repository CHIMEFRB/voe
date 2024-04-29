from typing import Any, Dict

import requests
from pydantic import Field

from frbvoe.models.voe import VOEvent


class TNS(VOEvent):
    """Transient Name Server (TNS) Report Object."""

    #! Rendered from FRB_VOE_TNS_API_KEY
    tns_api_key: str = Field(
        ..., description="API key for the TNS", example="1234567890"
    )
    tns_marker: str = Field(..., description="Marker for the TNS", example="FRB")
    tns_id: int = Field(..., description="ID for the TNS", example="1234567890")

    def submit(
        self, voevent: Dict[str, Any], api_key, tns_id, bot_name, tns_marker, url
    ):
        headers = {"User-Agent": tns_marker}
        json_data = {"api_key": api_key, "data": voevent}
        response = requests.post(url, headers=headers, data=json_data)
        response.raise_for_status()
        return response


# #! TODO: Functionality
# from frbvoe.models.voe import VOEvent

# voe = VOEvent(...)
# tns = TNS(**voe.payload)
