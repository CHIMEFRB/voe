import pytest

from frbvoe.models.subscriber import Subscriber


def test_create_subscriber():
    # Test creating a valid subscriber
    subscriber = Subscriber(
        name="John Smith",
        contact_email="john.smith@email.com",
        requested_service="emails",
    )
    assert subscriber.name == "John Smith"
    assert subscriber.contact_email == "john.smith@email.com"
    assert subscriber.requested_service == "emails"
    assert subscriber.subscriber_email is None
    assert subscriber.ip_address is None


def test_create_subscriber_with_optional_fields():
    # Test creating a subscriber with optional fields
    subscriber = Subscriber(
        name="Jane Doe",
        contact_email="jane.doe@email.com",
        requested_service="both",
        subscriber_email="voe.bot@email.com",
        ip_address="192.168.0.1",
    )
    assert subscriber.name == "Jane Doe"
    assert subscriber.contact_email == "jane.doe@email.com"
    assert subscriber.requested_service == "both"
    assert subscriber.subscriber_email == "voe.bot@email.com"
    assert subscriber.ip_address == "192.168.0.1"


def test_create_subscriber_with_invalid_fields():
    # Test creating a subscriber with invalid fields
    with pytest.raises(ValueError):
        Subscriber(
            name="", contact_email="invalid_email", requested_service="invalid_service"
        )
