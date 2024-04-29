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
    def report(self, voevent: Dict[str, Any], comet_url):
        """Sends a report using the given VOEvent and comet URL.

        Args:
            voevent (Dict[str, Any]): The VOEvent to send.
            comet_url (str): The URL of the comet to send the report to.
        """
        log.info("Sending VOE payload to Comet as a report.")
        report(voevent, comet_url)

    @property
    def retract(self, comet_url):
        """Retract the FRB from the Comet server."""
        log.info("Sending VOE payload to Comet as a retraction.")
        retract(self.dict(), comet_url)

    @property
    def update(self, comet_url):
        """Update the FRB on the Comet server."""
        log.info("Sending VOE payload to Comet as an update.")
        update(self.dict(), comet_url)


# TODO: Functionality
# from frbvoe.models.voe import VOEvent

# voe = VOEvent(...)
# tns = TNS(**voe.payload)
