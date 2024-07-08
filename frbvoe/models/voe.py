"""Virtual Observatory Event (VOEvent) Model."""

# from datetime import datetime
from typing import Any, Dict, Literal, Optional

import picologging as logging
import requests
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    SecretStr,
    StrictFloat,
    StrictInt,
    StrictStr,
)

# from pydantic_settings import BaseSettings, SettingsConfigDict
from sanic import Request

from frbvoe.utilities.email import send_email  # TODO: check this import

logging.basicConfig()
log = logging.getLogger()


class VOEvent(BaseModel):  # BaseSettings
    """VOEvent Object.
    Args:
        BaseSettings (BaseSettings): Pydantic BaseSettings.

    Attributes:
        kind (str): Which kind of VOEvent. Required.
        observatory_name (str): Name of the host observatory. Required.
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
        bits_per_sample (int) : Bits per sample of the observation. Optional.
        gain (float): Gain of the observation. Optional.
        tsys (float): System temperature of the observation. Optional.
        internal_id (str): Internal ID of the FRB. Optional.
        dm (float): Dispersion measure of the observation. Optional.
        dm_error (float): Error in the dispersion measure. Optional.
        width (float): Width of the pulse. Optional.
        snr (float): Signal-to-noise ratio of the observation. Optional.
        flux (float): Flux of the observation. Optional.
        coordinate_system (str): Coordinate system of the observation. Required.
        time (datetime): Time of the observation. Required.
        right_ascension (float): Right ascension of the observation. Required.
        declination (float): Declination of the observation. Required.
        pos_error_deg_95 (float): 95% localization error of the observation. Optional.
        importance (float): Importance of the observation between 0 and 1. Optional.
        website (str): Website of the host observatory. Optional.
        tns_name (str): TNS name of the event. Optional.

    Tokenized Attributes:
        comet_port (SecretInt) : Port of the comet broker. Optional
        email_password (SecretStr) : VOEvent author email account password. Optional.

    Raises:
        ValueError: If the voevent is not valid.

    Returns:
        VOEvent: VOEvent object.
    """

    # model_config = SettingsConfigDict(  # TODO: Shiny is this needed?
    #     title="FRB VOEvent",
    #     validate_assignment=True,
    #     validate_return=True,
    #     revalidate_instances="always",
    #     # This parameter ignores any extra fields that are not defined in the model
    #     extra="ignore",
    # )
    comet_port: int = Field(
        default=8098, description="Port of the Comet broker. Default is 8098. Optional."
    )
    email_password: SecretStr = Field(
        default=None, description="VOEvent author email account password. Optional."
    )
    kind: Literal[
        "detection",
        "subsequent",
        "retraction",
        "update",
    ] = Field(..., description="Which kind of VOEvent. Required.", example="detection")
    observatory_name: StrictStr = Field(
        ..., description="Name of the host observatory. Required.", example="CHIME"
    )
    # date: datetime = Field(
    #     ...,
    #     gt=datetime(2024, 1, 1),  # release date of frb-voe
    #     description="Detection time of the FRB. Required.",
    #     example="2020-01-13 16:55:08.844845",
    # )
    date: StrictStr = Field(
        ...,
        # release date of frb-voe
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
    bits_per_sample: int = Field(
        default=None,
        gt=0,
        description="Bits per sample of the observatory. Optional.",
        example=8,
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
    internal_id: StrictStr = Field(
        default=None,
        description="Internal ID of the FRB. Optional.",
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
        default=None,
        ge=0.0,
        le=360.0,
        description="""Right acension of the FRB in degrees
        in degrees (0 < RA < 360). Required.""",
        example=55.2938,
    )
    declination: float = Field(
        default=None,
        ge=-90.0,
        le=90.0,
        description="Declination of the FRB in degrees (-90 ≤ Dec ≤ 90). Required.",
        example=14.2049,
    )
    pos_error_deg_95: Optional[StrictFloat] = Field(
        default=None,
        gt=0.0,
        description="95% localization error of the observation. Required.",
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
        example="https://host_observatory.com/",
    )
    tns_name: Optional[StrictStr] = Field(
        default=None,
        description="Transient Name Server name of the FRB. Optional.",
        example="FRB20210826A",
    )
    update_message: StrictStr = Field(
        default=None,
        description="Custom email message to send in an update VOEvent. Optional.",
    )

    @property  # this just makes "payload" an attribute of the class
    def payload(self):
        """Return the VOEvent payload."""
        log.info("Returning VOEvent payload")
        return self.dict()

    @property
    def send_comet(comet_report: Dict[str, Any]):
        """Sends a report using the given VOEvent and comet URL.

        Args:
            voevent (Dict[str, Any]): The VOEvent to send.
            comet_url (str): The URL of the comet to send the report to.
            comet_port (SecretInt) : Port of the comet broker. Optional
        """
        log.info("Sending VOE payload to Comet as a report.")
        # vp.dump(voevent=comet_report, xml_declaration=False, file="temp_voe.txt")
        response = requests.post(
            "http://comet:8098/", json=comet_report
        )  # TODO: check comet endpoint
        return response.status_code == 200

    @property
    def send_email(email_report: Dict[str, Any]):
        """Sends the VOEvent email.

        Args:
            voevent (Dict[str, Any]): The VOEvent data.

        Returns:
            status (str): The status of the email.
        """
        log.info("Emailing VOE payload to subscribers.")
        send_email(email_report)

    @staticmethod  # TODO: Shiny what's this for?
    async def compile(request: Request):
        """Extracts data from request and returns object.

        Parameters
        ----------
        request : Request
            Sanic Request.

        Returns
        -------
        ActionData
            Object containing dependency data to take actions.
        """
        await request.receive_body()
        voe = request.json
        return VOEvent(**voe)
