"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging
from pydantic import Field, SecretStr

from frbvoe.models.voe import VOEvent
from frbvoe.utilities.email import report, retract, update

logging.basicConfig()
log = logging.getLogger()


class Email(VOEvent):
    """Represents an email object for sending VOEvents.

    Tokenized Attributes:
        email_username (SecretStr) : VOEvent author email account username. Optional.
        email_password (SecretStr) : VOEvent author email account password. Optional.
    """

    email_username: SecretStr = Field(
        default=None, description="VOEvent author email account username. Optional."
    )
    email_password: SecretStr = Field(
        default=None, description="VOEvent author email account password. Optional."
    )

    @property
    def report(voevent: Dict[str, Any]):
        """Sends the VOEvent email.

        Args:
            voevent (Dict[str, Any]): The VOEvent data.

        Returns:
            None
        """
        # subject = "Subject"
        # email_message = "This is the email"
        log.info("Sending VOE payload to Email as a report.")
        report(voevent)

    @property
    def retract(voevent: Dict[str, Any]):
        """Retract the FRB from the Comet server."""
        # subject = "Subject"
        # email_message = "This is the email"
        log.info("Sending VOE payload to Email as a retraction.")
        retract(voevent)

    @property
    def update(voevent: Dict[str, Any]):
        """Update the FRB on the Comet server."""
        # subject = "Subject"
        # email_message = "This is the email"
        log.info("Sending VOE payload to Email as an update.")
        update(voevent)
