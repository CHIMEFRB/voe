"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging
from pydantic import Field
from utilities.comet import report, retract, update

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


class Comet(VOEvent):
    """Represents a comet object that extends the VOEvent class.

    Attributes:
        url (str): The URL of the comet.
    """

    url: str = Field(..., description="Comet URL", example="comet.com")

    @property
    def report(voevent: Dict[str, Any]):
        """Sends a report using the given VOEvent and comet URL.

        Args:
            voevent (Dict[str, Any]): The VOEvent to send.
            comet_url (str): The URL of the comet to send the report to.
        """
        log.info("Sending VOE payload to Comet as a report.")
        report(voevent)

    @property
    def retract(voevent: Dict[str, Any]):
        """Retract the FRB from the Comet server."""
        log.info("Sending VOE payload to Comet as a retraction.")
        retract(voevent)

    @property
    def update(voevent: Dict[str, Any]):
        """Update the FRB on the Comet server."""
        log.info("Sending VOE payload to Comet as an update.")
        update(voevent)
