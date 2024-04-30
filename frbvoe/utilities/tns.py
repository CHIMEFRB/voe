"""Routines for TNS interactions."""

import logging

# from typing import Union


logging.basicConfig(format="%(levelname)s:%(message)s")
log = logging.getLogger(__name__)


def submit(voevent, api_key, tns_id, bot_name, tns_marker, url):
    """Submits a VOEvent to the Transient Name Server (TNS) API.

    Args:
        voevent (str): The VOEvent XML data to be submitted.
        api_key (str): The API key for authentication.
        tns_id (str): The TNS ID associated with the event.
        bot_name (str): The name of the bot submitting the event.
        tns_marker (str): The TNS marker associated with the event.
        url (str): The URL of the TNS API endpoint.

    Returns:
        requests.Response: The response object from the TNS API.
    """
    # headers = {"User-Agent": tns_marker}
    # json_data = {"api_key": api_key, "data": voevent}
    # response = requests.post(url, headers=headers, data=json_data)
    # return response
    pass
