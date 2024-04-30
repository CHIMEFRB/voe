"""Comet VOEvent broker."""


def report(voevent):
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
    return voevent


def retract(voevent):
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


def update(voeventl):
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
