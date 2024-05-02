"""Comet VOEvent broker."""

import voeventparse as vp


def send(voevent):
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
    vp.dump(voevent=voevent, xml_declaration=False, file="temp_voe.txt")
    # TODO send to comet

    return voevent
