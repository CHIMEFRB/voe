"""Tests for the Email model."""

import pytest
from pydantic import ValidationError

from frbvoe.models.subscriber import Subscriber

sample_request = {
    "kind": "detection",
    "name": "John Smith",
    "contact_email": "john.smith@email.com",
    "requested_service": "emailz",  # typo
    "subscriber_email": "voe.receiver@email.com",
    "ip_address": "0.0.0.0",
}


def test_subscriber():
    with pytest.raises(ValidationError):
        Subscriber(**sample_request)
