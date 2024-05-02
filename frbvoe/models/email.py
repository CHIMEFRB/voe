"""format a VOE for a TNS submission."""

import picologging as logging
from typing import Any, Dict
from pydantic import Field, SecretStr, StrictStr

from frbvoe.models.voe import VOEvent
from frbvoe.utilities.email import send

logging.basicConfig()
log = logging.getLogger()


class Email(VOEvent):
    """Represents an email object for sending VOEvents.

    Tokenized Attributes:
        email_password (SecretStr) : VOEvent author email account password. Optional.
    """
    email_password: SecretStr = Field(
        default=None, 
        description="VOEvent author email account password. Optional."
    )
    update_message: StrictStr = Field(
        default=None,
        description="Custom email message to send in an update VOEvent. Optional."
    )
    @property
    def send_to_subscribers(email_report: Dict[str, Any]):
        """Sends the VOEvent email.

        Args:
            voevent (Dict[str, Any]): The VOEvent data.

        Returns:
            status (str): The status of the email.
        """
        log.info("Emailing VOE payload to subscribers.")
        send(email_report)