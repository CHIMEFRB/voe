"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging
import requests
from pydantic import Field
from pydantic_settings import SettingsConfigDict

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


class TNS(VOEvent):
    """Represents a TNS (Transient Name Server) object.

    Tokenized Attributes:
        period (float): Proprietary period (in years) of the event on the TNS.
                        Defaults to 1 year.
        sandbox (bool): If True, use the TNS sandbox. Defaults to True.
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
    period: float = Field(
        default=1,
        gt=0.0,
        lt=100.0,
        description="""Proprietary period in years of the event on the TNS.
                    Defaults to 1 year.""",
        example=2.5,
    )
    sandbox: bool = Field(
        default=True,
        description="""If True, use the TNS sandbox. Defaults to True.""",
        example=True,
    )
    tns_api_key: str = Field(  # consider changing to SecretStr
        ...,
        description="API key for the TNS. Required.",
    )
    tns_report_id: int = Field(
        ..., description="Report ID for the TNS submission. Required."
    )
    tns_bot_name: str = Field(..., description="Name of the TNS bot. Required.")

    @property
    def search(tns_report: Dict[str, Any]):
        """Searches the TNS API for a specific event.

        Args:
            tns_report (Dict[str, Any]): The TNS report data to be searched.

        Returns:
            The response from the TNS API.

        Raises:
            requests.HTTPError: If the request to the TNS API fails.
        """
        url = "http://0.0.0.0:4357/v1/voe/tns/search"
        internal_name = tns_report["internal_name"]
        print(f"Searching TNS for object with internal name '{internal_name}'")
        tns_name = requests.post(url, json={"internal_name": internal_name}).json()[
            "tns_name"
        ]
        return tns_name

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
        # Make the JSON report
        url = "https://sandbox.wis-tns.org/api/bulk-report-form"
        headers = {"User-Agent": tns_report["tns_bot_name"]}
        json_data = {"api_key": tns_report["tns_api_key"], "data": tns_report}
        log.info("Sending VOE payload to TNS.")
        resp = requests.post(url=url, headers=headers, json=json_data)
        status = resp.status_code
        assert status == 200, f"Bad response status code: {status}"
        resp_json = resp.json()
        print(f"Got response from backend: {resp_json}")
        tns_name = resp_json["tns_name"]
        assert (
            tns_name is not None
        ), "TNS rejected submission, retain report ID if this persists."

        return tns_name
