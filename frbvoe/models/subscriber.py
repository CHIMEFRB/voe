"""Subscriber Model."""

from typing import Literal

import picologging as logging
from pydantic import BaseModel, EmailStr, Field, StrictStr

logging.basicConfig()
log = logging.getLogger()


class Subscriber(BaseModel):  # BaseSettings
    """Subscriber Object.

    Args:
        BaseSettings (BaseSettings): Pydantic BaseSettings.

    Attributes:
        name (str): Name of the subscriber. Required.
        contact_email (EmailStr): Contact email address of the subscriber. Required.
        requested_service (str): Requested service of the subscriber. Required.
        subscriber_email (EmailStr): Email address to send VOEvents to. Optional.
        ip_address (str): IP address of the subscriber. Optional.

    Raises:
        ValueError: If the subscriber parameters are not valid.

    Returns:
        Subscriber: Subscriber object.
    """

    name: StrictStr = Field(
        ..., description="Name of the subscriber. Required.", example="John Smith"
    )
    contact_email: EmailStr = Field(
        ...,
        description="Contact email address of the subscriber. Required.",
        example="john.smith@email.com",
    )
    requested_service: Literal[
        "emails",
        "xmls",
        "both",
    ] = Field(
        ...,
        description="Requested service of the subscriber. Required.",
        example="emails",
    )
    subscriber_email: EmailStr = Field(
        default=None,
        description="Email address to send VOEvents to. Optional.",
        example="voe.bot@email.com",
    )
    ip_address: StrictStr = Field(
        default=None, description="IP address of the subscriber. Optional."
    )
