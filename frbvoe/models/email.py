"""format a VOE for a TNS submission."""

from typing import Any, Dict

import picologging as logging
from pydantic import Field, SecretStr

from frbvoe.models.voe import VOEvent
from frbvoe.utilities.email import send_email

logging.basicConfig()
log = logging.getLogger()


class Email(VOEvent):
    """Represents an email object for sending VOEvents.

    Tokenized Attributes:
        email_password (SecretStr) : VOEvent author email account password. Optional.
    """

    # email_password: SecretStr = Field(
    #     default=None,
    #     description="VOEvent author email account password. Optional."
    # )

    @property
    def send(email_report: Dict[str, Any]):
        """Sends the VOEvent email.

        Args:
            voevent (Dict[str, Any]): The VOEvent data.

        Returns:
            status (str): The status of the email.
        """
        log.info("Emailing VOE payload to subscribers.")
        send_email(email_report)
