"""Send  submission."""

from typing import Any, Dict

import picologging as logging
import requests
from pydantic import Field

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


class Comet(VOEvent):
    """Represents a comet object that extends the VOEvent class.

    Tokenized Attributes:
        comet_port (SecretInt) : Port of the comet broker. Optional
    """

    # model_config = SettingsConfigDict(  # TODO: Shiny is this needed?
    #     title="FRB VOEvent",
    #     validate_assignment=True,
    #     validate_return=True,
    #     revalidate_instances="always",
    #     # This parameter ignores any extra fields that are not defined in the model
    #     extra="ignore",
    # )
    comet_port: int = Field(
        default=8098, description="Port of the Comet broker. Default is 8098. Optional."
    )

    @property
    def send(comet_report: Dict[str, Any]):
        """Sends a report using the given VOEvent and comet URL.

        Args:
            voevent (Dict[str, Any]): The VOEvent to send.
            comet_url (str): The URL of the comet to send the report to.
        """
        log.info("Sending VOE payload to Comet as a report.")
        # vp.dump(voevent=comet_report, xml_declaration=False, file="temp_voe.txt")
        response = requests.post(
            "http://comet:8098/", json=comet_report
        )  # TODO: check comet endpoint
        return response.status_code == 200
