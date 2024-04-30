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
        kind (str): Which kind of VOEvent. Required.
            - One of: detection, subsequent, retraction, or update
        *token (SecretStr): Github Personal Access Token. Optional*
        author (str): Name of the VOEvent author. Required.
        date (datetime): Detection time of the FRB. Required.
        email (EmailStr): Email address of the VOEvent author. Required.
        semi_major (float): Semi-major axis of the error ellipse of the
        host observatory's beam. Optional.
        semi_minor (float): Semi-minor axis of the error ellipse of the
        host observatory's beam. Optional.
        sampling_time (float): Sampling time of the observation. Optional.
        bandwidth (float): Bandwidth of the observation. Optional.
        central_frequency (float): Central frequency of the observation. Optional.
        npol (int): Number of polarizations of the observation. Optional.
        gain (float): Gain of the observation. Optional.
        tsys (float): System temperature of the observation. Optional.
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
        website (str): Website of the host observatory. Optional.
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
    ] = Field(..., description="Which kind of VOEvent. Required.", example="detection")
    author: StrictStr = Field(
        ..., description="Name of the VOEvent author. Required.", example="John Smith"
    )
    date: datetime = Field(
        ...,
        gt=datetime(2024, 5, 1),  # release date of frb-voe
        description="Detection time of the FRB. Required.",
        example="2020-01-13 16:55:08.844845",
    )
    email: EmailStr = Field(
        ...,
        description="Email address of the VOEvent author. Required.",
        example="john.smith@email.com",
    )
    semi_major: float = Field(
        default=None,
        gt=0.0,
        description="""Semi-major axis of the error ellipse
        of the host observatory's beam in degrees. Optional.""",
        example=0.026,
    )
    semi_minor: float = Field(
        default=None,
        gt=0.0,
        description="""Semi-minor axis of the error ellipse
        of the host observatory's beam in degrees. Optional.""",
        example=0.013,
    )
    sampling_time: float = Field(
        default=None,
        gt=0.0,
        description="Sampling time of the observation in seconds. Optional.",
        example=0.001,
    )
    bandwidth: float = Field(
        default=None,
        gt=0.0,
        description="Bandwidth of the observatory in MHz. Optional.",
        example=400,
    )
    central_frequency: float = Field(
        default=None,
        gt=0.0,
        description="Central frequency of the observatory in MHz. Optional.",
        example=600,
    )
    npol: StrictInt = Field(
        default=None,
        gt=0,
        description="Number of polarizations of the observation. Optional.",
        example=2,
    )
    gain: float = Field(
        default=None,
        description="Gain of the observatory in dB. Optional.",
        example=1.76,
    )
    tsys: float = Field(
        default=None,
        gt=0.0,
        description="System temperature of the observatory in K. Optional.",
        example=25.0,
    )
    dm: float = Field(
        default=None,
        gt=0.0,
        description="Dispersion measure of the FRB in pc/cm^3. Optional.",
        example=298.53,
    )
    dm_error: float = Field(
        default=None,
        gt=0.0,
        description="Error of the dispersion measure of the FRB in pc/cm^3. Optional.",
        example=0.01,
    )
    width: float = Field(
        default=None,
        description="Width in time of the FRB in s. Optional.",
        example=4.8,
    )
    snr: float = Field(
        default=None,
        description="Signal-to-noise ratio of the FRB. Optional.",
        example=13.8,
    )
    flux: float = Field(
        default=None, description="Flux of the FRB in Jy. Optional.", example=4.9
    )
    right_ascension: float = Field(
        ge=0.0,
        le=360.0,
        description="""Right acension of the FRB in degrees
        in degrees (0 < RA < 360). Required.""",
        example=55.2938,
    )
    declination: float = Field(
        ge=-90.0,
        le=90.0,
        description="Declination of the FRB in degrees (-90 ≤ Dec ≤ 90). Required.",
        example=14.2049,
    )
    localization_error: Optional[StrictFloat] = Field(
        default=None,
        gt=0.0,
        description="Error of the localization region in degrees. Required.",
        example=0.001,
    )
    importance: float = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Importance of the FRB (0 < Importance < 1). Optional.",
        example=0.9979,
    )
    website: Optional[StrictStr] = Field(
        default=None,
        description="Link to the host observatory website. Optional.",
    )
    tns_name: Optional[StrictStr] = Field(
        default=None,
        description="Transient Name Server name of the FRB. Optional.",
        example="FRB20210826A",
    )

    @property
    def payload(self):
        """Return the VOEvent payload."""
        log.info("Returning VOEvent payload")
        return self.dict()


# TODO: Functionality
# from frbvoe.models.voe import VOEvent

# voe = VOEvent(...)
# tns = TNS(**voe.payload)
