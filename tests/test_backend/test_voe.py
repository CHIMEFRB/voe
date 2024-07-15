import pytest

from frbvoe.models.voe import VOEvent


def test_voevent_creation():
    # Test valid VOEvent creation
    voevent = VOEvent(
        kind="detection",
        observatory_name="CHIME",
        date="2020-01-13 16:55:08.844845",
        email="john.smith@email.com",
        right_ascension=55.2938,
        declination=14.2049,
        pos_error_deg_95=0.001,
        importance=0.9979,
    )
    assert voevent.kind == "detection"
    assert voevent.observatory_name == "CHIME"
    assert voevent.date == "2020-01-13 16:55:08.844845"
    assert voevent.email == "john.smith@email.com"
    assert voevent.right_ascension == 55.2938
    assert voevent.declination == 14.2049
    assert voevent.pos_error_deg_95 == 0.001
    assert voevent.importance == 0.9979

    # Test invalid VOEvent creation with missing required fields
    with pytest.raises(ValueError):
        voevent = VOEvent(kind="detection", observatory_name="CHIME")

    # Test invalid VOEvent creation with invalid field values
    with pytest.raises(ValueError):
        voevent = VOEvent(
            kind="invalid_kind",
            observatory_name="CHIME",
            date="2020-01-13 16:55:08.844845",
            email="invalid_email",
            right_ascension=55.2938,
            declination=14.2049,
            pos_error_deg_95=0.001,
            importance=0.9979,
        )
