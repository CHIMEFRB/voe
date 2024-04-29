"""Comet VOEvent broker."""

import requests


def report(voevent, comet_url):
    """Report the FRB to the Comet server."""
    # # Format the Comet request
    # voevent["role"] = "observation"
    # voevent["stream"] = "chime-frb"
    # # Send the VOEvent to the Comet server
    # response = requests.post(comet_url, json=voevent)
    # # Check if the request was successful
    # if response.status_code == 200:
    #     return True
    # else:
    #     return False
    return comet_url + " " + voevent


def retract(voevent, comet_url):
    """Retract the FRB from the Comet server."""
    # # Format the Comet request
    # voevent["role"] = "retraction"
    # voevent["stream"] = "chime-frb"
    # # Send the VOEvent to the Comet server
    # response = requests.post(comet_url, json=voevent)
    # # Check if the request was successful
    # if response.status_code == 200:
    #     return True
    # else:
    #     return False
    pass


def update(voevent, comet_url):
    """Update the FRB on the Comet server."""
    # # Format the Comet request
    # voevent["role"] = "update"
    # voevent["stream"] = "chime-frb"
    # # Send the VOEvent to the Comet server
    # response = requests.post(comet_url, json=voevent)
    # # Check if the request was successful
    # if response.status_code == 200:
    #     return True
    # else:
    #     return False
    pass
