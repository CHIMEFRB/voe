import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def report(voevent, sender_email, password, subject, message):
    """Send the VOEvent via email."""

    # Email configuration
    sender_email = 'your_email@example.com'
    receiver_emails = ["personA@email.com", "person_B@email.com"]
    # Format the email message
    message = 'Message to be sent via email'

    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)  # Example for Gmail: smtp.gmail.com, port 587
    server.starttls()  # Secure the connection

    # Login to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_emails, msg.as_string())

    # Close the connection
    server.quit()
    
def retract(voevent, sender_email, password, subject, message):
    """Send the VOEvent retraction via email."""

    # Email configuration
    sender_email = 'your_email@example.com'
    receiver_emails = ["personA@email.com", "person_B@email.com"]
    # Format the email message
    message = 'Message to be sent via email'

    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)  # Example for Gmail: smtp.gmail.com, port 587
    server.starttls()  # Secure the connection

    # Login to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_emails, msg.as_string())

    # Close the connection
    server.quit()
    
def update(voevent, sender_email, password, subject, message):
    """Send the VOEvent update via email."""

    # Email configuration
    sender_email = 'your_email@example.com'
    receiver_emails = ["personA@email.com", "person_B@email.com"]
    # Format the email message
    message = 'Message to be sent via email'

    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)  # Example for Gmail: smtp.gmail.com, port 587
    server.starttls()  # Secure the connection

    # Login to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_emails, msg.as_string())

    # Close the connection
    server.quit()
    
