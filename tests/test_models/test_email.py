"""Tests for the Email model."""

import pytest
from pydantic import ValidationError

from frbvoe.models.email import Email

sample_request = {
    "kind": "detection",
    "date": "2025-01-13 16:55:08.844845",
    "email": "john.smith@email.com",
    "semi_major": 0.026,
    "semi_minor": 0.013,
    "sampling_time": 0.001,
    "bandwidth": 400,
    "central_frequency": 600,
    "npol": 2,
    "bits_per_sample": 2,
    "gain": 1.76,
    "tsys": 25.0,
    "internal_id": "20210826A",
    "dm": 298.53,
    "dm_error": 0.01,
    "width": 4.8,
    "snr": 13.8,
    "flux": 4.9,
    "right_ascension": 55.2938,
    "declination": 14.2049,
    "pos_error_deg_95": 0.1,
    "importance": 0.9979,
    "website": "https://www.example.com",
    "tns_name": "FRB20210826A",
    "update_message": "",
}


def test_email():
    with pytest.raises(ValidationError):
        Email(**sample_request)
