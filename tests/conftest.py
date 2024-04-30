"""Testing for VOEvent object."""

import datetime

import pytest

from frbvoe.models.voe import VOEvent


@pytest.fixture
def voe():
    """Generate a VOEvent object for testing.

    Returns:
        VOEvent: VOEvent object.
    """
    return VOEvent(
        kind="detection",
        author="John Smith",
        email="john.smith@email.com",
        coordinate_system="celestial",
        right_ascension=55.2938,
        declination=14.2049,
        localization_error=0.1,
        importance=0.9979,
        website="https://www.example.com",
        backend_url="https://www.example.com/backend",
        tns_name="FRB20210826A",
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        semi_major=0.026,
        semi_minor=0.013,
        ellipse_error=0.001,
        sampling_time=0.001,
        bandwidth=400,
        central_frequency=600,
        npol=2,
        bits_per_sample=2,
        gain=1.76,
        tsys=25.0,
        beam_number=2,
        dm=298.53,
        dm_error=0.01,
        width=4.8,
        snr=13.8,
        flux=4.9,
    )
