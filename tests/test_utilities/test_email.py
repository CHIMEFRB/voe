import unittest
from unittest.mock import patch
from frbvoe.utilities import email

class TestEmailUtility(unittest.TestCase):

    @patch('frbvoe.utilities.email.logging')
    def test_send_email(self, mock_logging):
        # Test sending email with valid email_report
        email_report = {
            'backend': 'backend_name',
            'internal_id': '123',
            'tns_name': 'FRB123',
            'dm': 100,
            'dm_error': 1,
            'date': '2022-01-01 12:00:00',
            'snr': 10,
            'pos_error_deg_95': 0.1,
            'coordinate_system': 'J2000',
            'ra': 180,
            'dec': 45,
            'website': 'https://observatory.com',
            'importance': 'high'
        }
        with patch('frbvoe.utilities.email.smtplib') as mock_smtplib:
            email.send_email(email_report)
            # Assert that the email is sent using smtplib
            mock_smtplib.SMTP.assert_called_once()
            # Assert that the email content is formatted correctly
            mock_smtplib.SMTP().sendmail.assert_called_once_with(
                'sender@example.com',
                'receiver@example.com',
                'Subject: FRB Report\n\n'
                'FRB Report:\n'
                '\tbackend: backend_name\n'
                '\n'
                '\tevent parameters:\n'
                '\t\tevent_no: 123\n'
                '\n'
                '\t\tknown_source_name: FRB123\n'
                '\n'
                '\t\tdm: 100 +/- 1 pc/cm^3\n'
                '\n'
                '\t\ttimestamp_utc: 2022-01-01 12:00:00\n'
                '\n'
                '\t\tsnr: 10\n'
                '\n'
                '\t\tpos_error_deg_95: 0.1 degrees\n'
                '\n\n'
                'WHERE and WHEN\n'
                '\tCoordinate system: J2000\n'
                '\tTimestamp [UTC]: 2022-01-01 12:00:00\n'
                '\tLocalization: (180, 45) +/- 0.1 degrees (J2000)\n'
                '\n\n'
                'HOW\n'
                '\tDescription: info about the observatory: https://observatory.com\n'
                '\n\n'
                'WHY\n'
                '\tImportance: high\n'
                '\n\n'
            )
            # Assert that the logger is called correctly
            mock_logging.getLogger().info.assert_called_once_with('Email sent successfully.')

    @patch('frbvoe.utilities.email.logging')
    def test_send_email_invalid_report(self, mock_logging):
        # Test sending email with invalid email_report
        email_report = {
            'backend': 'backend_name',
            'internal_id': '123',
            'tns_name': 'FRB123',
            'dm': 100,
            'dm_error': 1,
            'date': '2022-01-01 12:00:00',
            'snr': 10,
            'pos_error_deg_95': 0.1,
            'coordinate_system': 'J2000',
            'ra': 180,
            'dec': 45,
            'website': 'https://observatory.com',
            'importance': 'high'
        }
        with patch('frbvoe.utilities.email.smtplib') as mock_smtplib:
            # Raise an exception when sending email
            mock_smtplib.SMTP().sendmail.side_effect = Exception('Failed to send email')
            email.send_email(email_report)
            # Assert that the email is sent using smtplib
            mock_smtplib.SMTP.assert_called_once()
            # Assert that the email content is formatted correctly
            mock_smtplib.SMTP().sendmail.assert_called_once_with(
                'sender@example.com',
                'receiver@example.com',
                'Subject: FRB Report\n\n'
                'FRB Report:\n'
                '\tbackend: backend_name\n'
                '\n'
                '\tevent parameters:\n'
                '\t\tevent_no: 123\n'
                '\n'
                '\t\tknown_source_name: FRB123\n'
                '\n'
                '\t\tdm: 100 +/- 1 pc/cm^3\n'
                '\n'
                '\t\ttimestamp_utc: 2022-01-01 12:00:00\n'
                '\n'
                '\t\tsnr: 10\n'
                '\n'
                '\t\tpos_error_deg_95: 0.1 degrees\n'
                '\n\n'
                'WHERE and WHEN\n'
                '\tCoordinate system: J2000\n'
                '\tTimestamp [UTC]: 2022-01-01 12:00:00\n'
                '\tLocalization: (180, 45) +/- 0.1 degrees (J2000)\n'
                '\n\n'
                'HOW\n'
                '\tDescription: info about the observatory: https://observatory.com\n'
                '\n\n'
                'WHY\n'
                '\tImportance: high\n'
                '\n\n'
            )
            # Assert that the logger is called correctly
            mock_logging.getLogger().error.assert_called_once_with('Failed to send email.')

if __name__ == '__main__':
    unittest.main()