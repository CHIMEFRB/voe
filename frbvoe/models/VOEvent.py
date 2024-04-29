"""Virtual Observatory Event (VOEvent) Model."""

from datetime import datetime
from typing import Literal, Optional

from pydantic import StrictFloat  # , SecretStr
from pydantic import BaseModel, EmailStr, Field, StrictInt, StrictStr

from frbvoe.utilities import tns, comet, email

class VOEvent(BaseModel):
    """VOEvent Object.

    Args:
        BaseModel (BaseModel): Pydantic BaseModel.

    Attributes:
        # VOE Header
        voe_type (str): Type of the VOEvent. Required.
        *token (SecretStr): Github Personal Access Token. Optional*

        # Who Section
        author (str): Author name of the VOEvent. Required.
        date (datetime): Date of the VOEvent. Required.
        email (EmailStr): Email of the author. Required.

        # What Section
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

        # WhereWhen Section
        coordinate_system (str): Coordinate system of the observation. Required.
        time (datetime): Time of the observation. Required.
        right_ascension (float): Right ascension of the observation. Required.
        declination (float): Declination of the observation. Required.
        localization_error (float): Localization error of the observation. Optional.

        # Why Section
        importance (float): Importance of the observation between 0 and 1. Optional.

        # How Section (Optional)
        website (str): Website of the author observatory. Optional.
        backend_url (str): Backend URL of the author observatory. Optional.

        # Citations
        tns_name (str): TNS name of the event. Optional.

    Raises:
        ValueError: If the voevent is not valid.

    Returns:
        VOEvent: VOEvent object.

    TODO: example usage

    """

    voe_type: Literal[
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
    def tns_submit(self, api_key, tns_id, bot_name, tns_marker, url):
        """Submit the VOEvent to the Transient Name Server."""

        tns.submit(self.dict(), api_key, tns_id, bot_name, tns_marker, url)
    def comet_report(self, comet_url):
        """Report the FRB to the Comet server."""
            
        comet.report(self.dict(), comet_url)
    def comet_retraction(self, comet_url):
        """Retract the FRB from the Comet server."""
            
        comet.retract(self.dict(), comet_url)
    def comet_update(self, comet_url):
        """Update the FRB on the Comet server."""
            
        comet.update(self.dict(), comet_url)
    def email_report(self, sender_email, receiver_email, password, subject, message):
        """Send the VOEvent via email."""
            
        email.report(self.dict(), sender_email, receiver_email, password, subject, message)
    def email_retraction(self, sender_email, receiver_email, password, subject, message):
        """Send the VOEvent retraction via email."""
            
        email.retract(self.dict(), sender_email, receiver_email, password, subject, message)
    def email_update(self, sender_email, receiver_email, password, subject, message):
        """Send the VOEvent update via email."""
            
        email.update(self.dict(), sender_email, receiver_email, password, subject, message)

# Example usage
sample_voe = VOEvent(
    voe_type="detection",
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
    date="2020-01-13 16:55:08.844845",
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
print(sample_voe)
