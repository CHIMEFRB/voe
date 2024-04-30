"""format a VOE for a TNS submission."""

import picologging as logging
# import requests
from pydantic import Field, SecretInt, SecretStr
from pydantic_settings import SettingsConfigDict
from typing import Any, Dict

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


class TNS(VOEvent):
    """Represents a TNS (Transient Name Server) object.

    Tokenized Attributes:
        tns_api_key (SecretStr): API key for the TNS. Required.
        tns_report_id (SecretInt): Report ID for the TNS submission. Required.
        tns_bot_name (SecretStr): Name of the TNS bot. Required.
    """
    model_config = SettingsConfigDict(
        title="TNS Report",
        validate_assignment=True,
        validate_return=True,
        revalidate_instances="always",
        env_prefix="TNS_",
        # This parameter ignores any extra fields that are not defined in the model
        extra="ignore",
    )
    tns_api_key: SecretStr = Field(
        ..., 
        description="API key for the TNS. Required.",
    )
    tns_report_id: SecretInt = Field(
        ..., 
        description="Report ID for the TNS submission. Required."
        )
    tns_bot_name: SecretStr = Field(
        ..., 
        description="Name of the TNS bot. Required."
        )
    @property
    def submit(tns_report: Dict[str, Any]):
        """Submits a VOEvent to the TNS API.

        Args:
            tns_report (Dict[str, Any]): The TNS report data to be submitted.

        Returns:
            The response from the TNS API.

        Raises:
            requests.HTTPError: If the request to the TNS API fails.
        """
        # headers = {"User-Agent": tns_marker}
        # json_data = {"api_key": api_key, "data": voevent}
        # log.info("Sending VOE payload to TNS.")
        # response = requests.post(url, headers=headers, data=json_data)
        # response.raise_for_status()
        # return response
        pass
