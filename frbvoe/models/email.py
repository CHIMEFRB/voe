"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging
import requests
from pydantic import Field
from utilities.email import report, retract, update

from frbvoe.models.voe import VOEvent

logging.basicConfig()
log = logging.getLogger()


class Email(VOEvent):
    """Represents an email object for sending VOEvents."""

    username: str = Field(..., description="API key for the TNS", example="1234567890")
    password: str = Field(..., description="Marker for the TNS", example="FRB")

    @property
    def report(self, voevent: Dict[str, Any]):
        """Sends the VOEvent email.

        Args:
            voevent (Dict[str, Any]): The VOEvent data.

        Returns:
            None
        """
        subject = "Subject"
        email_message = "This is the email"
        log.info("Sending VOE payload to Email as a report.")
        report(voevent, self.username, self.password, subject, email_message)

    @property
    def retract(self):
        """Retract the FRB from the Comet server."""
        subject = "Subject"
        email_message = "This is the email"
        log.info("Sending VOE payload to Email as a retraction.")
        retract(self.dict(), self.username, self.password, subject, email_message)

    @property
    def update(self):
        """Update the FRB on the Comet server."""
        subject = "Subject"
        email_message = "This is the email"
        log.info("Sending VOE payload to Email as an update.")
        update(self.dict(), self.username, self.password, subject, email_message)


# TODO: Functionality
# from frbvoe.models.voe import VOEvent

# voe = VOEvent(...)
# tns = TNS(**voe.payload)
