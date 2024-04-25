from datetime import datetime
from typing import Literal, Optional

from pydantic import StrictFloat  # , SecretStr
from pydantic import BaseModel, EmailStr, Field, StrictInt, StrictStr


class TNSReport(BaseModel):
    """TNSReport Object.

    Args:
        BaseModel (BaseModel): Pydantic BaseModel.

    Attributes:
        author (str): Author name of the VOEvent. Required.
        date (datetime): Date of the VOEvent. Required.
        email (EmailStr): Email of the author. Required.
        semi_major (float): Semi-major axis of the error ellipse. Optional.
        semi_minor (float): Semi-minor axis of the error ellipse. Optional.
        ellipse_error (float): Position angle of the error ellipse. Optional.
        sampling_time (float): Sampling time of the observation. Optional.
        bandwidth (float): Bandwidth of the observation. Optional.
        central_frequency (float): Central frequency of the observation. Optional.
        npol (int): Number of polarizations. Optional.
        bits_per_sample (int): Bits per sample. Optional.
        gain (float): Gain of the observation. Optional.
        tsys (float): System temperature of the observation. Optional.
        beam_number (int): Beam number of the observation. Optional.
        dm (float): Dispersion measure of the observation. Optional.
        dm_error (float): Error in the dispersion measure. Optional.
        width (float): Width of the pulse. Optional.
        snr (float): Signal-to-noise ratio of the observation. Optional.
        flux (float): Flux of the observation. Optional.
        coordinate_system (str): Coordinate system of the observation. Required.
        time (datetime): Time of the observation. Required.
        right_ascension (float): Right ascension of the observation. Required.
        declination (float): Declination of the observation. Required.
        localization_error (float): Localization error of the observation. Optional.
        importance (float): Importance of the observation between 0 and 1. Optional.
        website (str): Website of the author observatory. Optional.

    Raises:
        ValueError: If the report is not valid.

    Returns:
        TNSReport: TNSReport object.

    TODO: example usage

    """

    author: StrictStr = Field(
        ..., description="Author name of the VOEvent", example="John Smith"
    )
    date: datetime = Field(
        ...,
        description="Detection time of the FRB",
        example="2020-01-13 16:55:08.844845",
    )
    email: EmailStr = Field(
        ..., description="Email of the author.", example="john.smith@email.com"
    )
    semi_major: float = Field(
        default=None,
        description="Size of the telescope's beam's semi-major axis in degrees.",
        example=0.026,
    )
    semi_minor: float = Field(
        default=None,
        description="Size of the telescope's beam's semi-minor axis in degrees.",
        example=0.013,
    )
    ellipse_error: float = Field(
        default=None,
        description="Error of the telescope's beam ellipse in degrees.",
        example=0.001,
    )
    sampling_time: float = Field(
        default=None,
        description="Sampling time of the observation.",
        example=0.001,
    )
    sampling_time: float = Field(
        default=None,
        description="Bandwidth of the observatory in MHz.",
        example=400,
    )
    central_frequency: float = Field(
        default=None,
        description="Central frequency of the observatory in MHz",
        example=600,
    )
    npol: StrictInt = Field(
        default=None,
        description="Number of polarizations.",
        example=2,
    )
    bits_per_sample: StrictInt = Field(
        default=None,
        description="Number of bits per sample.",
        example=2,
    )
    gain: float = Field(
        default=None,
        description="Gain of the observatory in dB.",
        example=1.76,
    )
    tsys: float = Field(
        default=None,
        description="System temperature of the observatory in K.",
        example=25.0,
    )
    beam_number: int = Field(
        default=None,
        description="Number of the beam in which the FRB was detected (for multi-beam observatories).",
        example=2,
    )
    dm: float = Field(
        default=None,
        description="Dispersion measure of the FRB in pc/cm^3.",
        example=298.53,
    )
    dm_error: float = Field(
        default=None,
        description="Error of the dispersion measure of the FRB in pc/cm^3.",
        example=0.01,
    )
    width: float = Field(
        default=None,
        description="Width in time of the FRB in ms.",
        example=4.8,
    )
    snr: float = Field(
        default=None,
        description="Signal-to-noise ratio of the FRB.",
        example=13.8,
    )
    flux: float = Field(
        default=None,
        description="Flux of the FRB in Jy.",
        example=4.9,
    )
    coordinate_system: Literal[
        "celestial",
        "horizontal",
        "galactic",
    ] = Field(
        ...,
        description="Coordinate system for the WhereWhen section. Required.",
        example="celestial",
    )
    right_ascension: float = Field(
        ge=0.0,
        le=360.0,
        description="Right acension of the FRB in degrees (0 < RA < 360).",
        example=55.2938,
    )
    declination: float = Field(
        ge=-90.0,
        le=90.0,
        description="Declination of the FRB in degrees (-90 < Dec < 90).",
        example=14.2049,
    )
    localization_error: Optional[StrictFloat] = Field(
        default=None, description="Error of the localization region."
    )
    importance: float = Field(
        ge=0.0,
        le=1.0,
        description="Importance of the FRB (0 < Importance < 1).",
        example=0.9979,
    )
    website: Optional[StrictStr] = Field(
        default=None,
        description="Link to the observatory website",
    )
