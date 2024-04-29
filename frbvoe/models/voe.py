"""Virtual Observatory Event (VOEvent) Model."""

from datetime import datetime
from typing import Literal, Optional

import picologging as logging
from pydantic import EmailStr, Field, StrictFloat, StrictInt, StrictStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logging.basicConfig()
log = logging.getLogger()


class VOEvent(BaseSettings):
    """VOEvent Object.

    Args:
        BaseSettings (BaseSettings): Pydantic BaseSettings.

    Note:
        The selection priority for attributes in descending order is:

          - Arguments passed to the `VOEvent` Object.
          - Environment variables with `FRB_VOE_` prefix.
          - The default values in the class constructor.

    Attributes:
        kind (str): Kind of the VOEvent. Required.
            -One of: detection, subsequent, retraction, or update
        *token (SecretStr): Github Personal Access Token. Optional*
        author (str): Author name of the VOEvent. Required.
        email (EmailStr): Email address of the author. Required.
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
        tns_name (str): TNS name of the event. Optional.

    Raises:
        ValueError: If the voevent is not valid.

    Returns:
        VOEvent: VOEvent object.
    """

    model_config = SettingsConfigDict(
        title="FRB VOEvent",
        validate_assignment=True,
        validate_return=True,
        revalidate_instances="always",
        env_prefix="FRB_VOE_",
        # This parameters ignores any extra fields that are not defined in the model
        extra="ignore",
    )
    kind: Literal[
        "detection",
        "subsequent",
        "retraction",
        "update",
    ] = Field(
        ...,
        description="Type of VOEvent. Required.",
        example="detection",
    )
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
    bandwidth: float = Field(
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
        description="""
        Number of the beam in which the FRB was detected (for multi-beam observatories).
        """,
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
    backend_url: Optional[StrictStr] = Field(
        default=None,
        description="Link to more information about the observatory backend",
    )
    tns_name: Optional[StrictStr] = Field(
        default=None,
        description="Transient Name Server name of the FRB",
        example="FRB20210826A",
    )

    @property
    def payload(self):
        """Return the VOEvent payload."""
        log.info("Returning VOEvent payload")
        return self.dict()
