"""Function to send request to Comet."""

import requests

async def send_to_comet(payload) -> bool:
    response = requests.post("http://comet:8098/", json=payload)
    # ? Maybe you'll need to change this
    return response.status_code == 200
