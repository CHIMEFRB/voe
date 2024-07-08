from datetime import datetime

from frbvoe.models.voe import VOEvent


def test_voevent():
    # Create a valid VOEvent object
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

    # Check that the object is valid
    assert voevent.is_valid()

    # Check that the attributes are set correctly
    assert voevent.kind == "detection"
    assert voevent.observatory_name == "CHIME"
    assert voevent.date == datetime.strptime(
        "2020-01-13 16:55:08.844845", "%Y-%m-%d %H:%M:%S.%f"
    )
    assert voevent.email == "john.smith@email.com"
    assert voevent.right_ascension == 55.2938
    assert voevent.declination == 14.2049
    assert voevent.pos_error_deg_95 == 0.001
    assert voevent.importance == 0.9979

    # Check that optional attributes are set to None by default
    assert voevent.semi_major is None
    assert voevent.semi_minor is None
    assert voevent.sampling_time is None
    assert voevent.bandwidth is None
    assert voevent.central_frequency is None
    assert voevent.npol is None
    assert voevent.bits_per_sample is None
    assert voevent.gain is None
    assert voevent.tsys is None
    assert voevent.internal_id is None
    assert voevent.dm is None
    assert voevent.dm_error is None
    assert voevent.width is None
    assert voevent.snr is None
    assert voevent.flux is None
    assert voevent.website is None
    assert voevent.tns_name is None
    assert voevent.update_message is None

    # Check that tokenized attributes are set to None by default
    assert voevent.comet_port == 8098
    assert voevent.email_password is None
