"""Routines for TNS interactions."""

import logging
import requests
from typing import Union

logging.basicConfig(format="%(levelname)s:%(message)s")
log = logging.getLogger(__name__)


def submit(voevent, api_key, tns_id, bot_name, tns_marker, url):
    headers = {'User-Agent': tns_marker}
    json_data = {'api_key': api_key, 'data': voevent}
    response = requests.post(url, headers = headers, data = json_data)
    return response