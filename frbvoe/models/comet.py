"""format a VOE for a TNS submission."""

import picologging as logging
from typing import Any, Dict
from pydantic import Field, SecretInt

from frbvoe.models.voe import VOEvent
from utilities.comet import report, retract, update

logging.basicConfig()
log = logging.getLogger()

class Comet(VOEvent):
    """Represents a comet object that extends the VOEvent class.

    Tokenized Attributes:
        comet_port (SecretInt) : Port of the comet broker. Optional
    """
    comet_port : SecretInt = Field(
        default=None, 
        description= "Port of the comet broker. Optional."
    )
    @property
    def report(comet_report: Dict[str, Any]):
        """Sends a report using the given VOEvent and comet URL.

        Args:
            voevent (Dict[str, Any]): The VOEvent to send.
            comet_url (str): The URL of the comet to send the report to.
        """
        log.info("Sending VOE payload to Comet as a report.")
        report(comet_report)

    @property
    def retract(comet_report: Dict[str, Any]):
        """Retract the FRB from the Comet server."""
        log.info("Sending VOE payload to Comet as a retraction.")
        retract(comet_report)

    @property
    def update(comet_report: Dict[str, Any]):
        """Update the FRB on the Comet server."""
        log.info("Sending VOE payload to Comet as an update.")
        update(comet_report)
