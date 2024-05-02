"""this function sends an email."""

import smtplib
import picologging as logging
from typing import Any, Dict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logging.basicConfig()
log = logging.getLogger()

def send(email_report: Dict[str, Any]):
    """Send the VOEvent via email.

    Args:
        voevent: The VOEvent to be sent.
        sender_email: The email address of the sender.
        password: The password of the sender's email account.
        subject: The subject of the email.
        message: The message to be sent via email.
    """
    
    subject = f"{email_report.observatory_name}_VOE_{email_report.kind}"
    if email_report.kind in ["detection", "subsequent"]:
        email_message = f"""
            {email_report.kind}-type VOEvent\n
            \n
            WHO\n
            Produced: {email_report.date}\n
            \tVOEvent IVORN: ivo://ca.chimenet.frb/FRB-DETECTION-#2024-05-01-02:28:38.969602UTC+0000_8b25b68ebd77 #TODO\n
            \n
            WHAT\n
            \tobservatory parameters:\n
            \t\tsampling_time: {email_report.sampling_time if not None} s\n
            \n
            \t\tbandwidth: {email_report.bandwidth if not None} MHz\n
            \n
            \t\tcentre_frequency: {email_report.central_frequency if not None} MHz\n
            \n
            \t\tnpol: {email_report.npol if not None}\n
            \n
            \t\tbits_per_sample: {email_report.bits_per_sample if not None}\n
            \n
            \t\ttsys: {email_report.tsys if not None} K\n
            \n
            \t\tbackend: {email_report.backend if not None}\n
            \n
            \tevent parameters:\n
            \t\tevent_no: {email_report.internal_id if not None}\n
            \n
            \t\tknown_source_name: {email_report.tns_name if not None}\n
            \n
            \t\tdm: {email_report.dm} +/- {email_report.dm_error} pc/cm^3\n
            \n
            \t\ttimestamp_utc: {email_report.date} +/- {email_report.sampling_time}\n #TODO
            \n
            \t\tsnr: {email_report.snr}\n
            \n
            \t\tpos_error_deg_95: {email_report.pos_error_deg_95} degrees\n 
            \n\n
            WHERE and WHEN\n
            \tCoordinate system: {email_report.coordinate_system}\n
            \tTimestamp [UTC]: {email_report.date}\n
            \tLocalization: ({email_report.ra}, {email_report.dec}) +/- {email_report.pos_error_deg_95} degrees (J2000)\n
            \n\n
            HOW\n
            \tDescription: information regarding the host observatory can be found here: {email_report.website}\n
            \n\n
            WHY\n
            \tImportance: {email_report.importance}\n
            \n\n

            **********
            This email was generated automatically by the {email_report.observatory_name} frb-voe Service. Please direct comments, questions, and concerns to {email_report.email}.

            --
            You are receiving this email because you are currently a subscriber to the public {email_report.observatory_name} frb-voe Service. To unsubscribe, please contact {email_report.email}.
        """
    if email_report.kind == "retraction":
        email_message = f"""
            {email_report.kind}-type VOEvent\n
            \n
            WHO\n
            Produced: {email_report.date}\n
            \tVOEvent IVORN: ivo://ca.chimenet.frb/FRB-DETECTION-#2024-05-01-02:28:38.969602UTC+0000_8b25b68ebd77 #TODO\n
            \n
            WHAT\n
            WHERE and WHEN\n
            \tCoordinate system: {email_report.coordinate_system}\n
            \tTimestamp [UTC]: {email_report.date}\n
            \tLocalization: ({email_report.ra}, {email_report.dec}) +/- {email_report.pos_error_deg_95} degrees (J2000)\n
            \n\n
            HOW\n
            \tDescription: Human-issued retraction. For more information, see: {email_report.website}\n
            \n\n
            WHY\n
            CITATIONS\n
            \t{email_report.internal_id}\n

            **********
            This email was generated automatically by the {email_report.observatory_name} frb-voe Service. Please direct comments, questions, and concerns to {email_report.email}.

            --
            You are receiving this email because you are currently a subscriber to the public {email_report.observatory_name} frb-voe Service. To unsubscribe, please contact {email_report.email}.
        """
    if email_report.kind == "update":
        email_message = {email_report.update_message} 

    # Email configuration
    receiver_email = "thomas.abbott@mail.mcgill.ca" #TODO: load from DB
    smtp_server = "smtp.example.com" #TODO: Shiny what should this be?
    smtp_port = 587  # Change to the appropriate port if needed

    # Create a message
    message = MIMEMultipart()
    message['From'] = email_report.email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(email_message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(email_report.email, email_report.email_password)

    # Send the email
    server.send_message(message)

    # Quit the server
    server.quit()
    
    status = "Success"
    
    return status