import logging

import requests

# Define any parameters you want to send along with the request (if any)
detection_example_payload = {
    "kind": "detection",
    "date": "2025-01-13 16:55:08.844845",
    "email": "john.smith@email.com",
    "semi_major": 0.026,
    "semi_minor": 0.013,
    "sampling_time": 0.001,
    "bandwidth": 400,
    "central_frequency": 600,
    "npol": 2,
    "bits_per_sample": 2,
    "gain": 1.76,
    "tsys": 25.0,
    "internal_id": "38249195",
    "dm": 298.53,
    "dm_error": 0.01,
    "width": 4.8,
    "snr": 13.8,
    "flux": 4.9,
    "right_ascension": 55.2938,
    "declination": 14.2049,
    "pos_error_deg_95": 0.1,
    "importance": 0.9979,
    "website": "https://www.observatory.com",
}

subsequent_example_payload = {
    "kind": "subsequent",
    "date": "2025-01-13 16:55:08.844845",
    "email": "john.smith@email.com",
    "semi_major": 0.026,
    "semi_minor": 0.013,
    "sampling_time": 0.001,
    "bandwidth": 400,
    "central_frequency": 600,
    "npol": 2,
    "bits_per_sample": 2,
    "gain": 1.76,
    "tsys": 25.0,
    "internal_id": "38249195",
    "dm": 298.53,
    "dm_error": 0.01,
    "width": 4.8,
    "snr": 13.8,
    "flux": 4.9,
    "right_ascension": 55.2938,
    "declination": 14.2049,
    "pos_error_deg_95": 0.1,
    "importance": 0.9979,
    "website": "https://www.observatory.com",
    "tns_name": "FRB20210826A",
}

update_example_payload = {
    "kind": "update",
    "date": "2025-01-13 16:55:08.844845",
    "email": "john.smith@email.com",
    "internal_id": "38249195",
    "tns_name": "FRB20210826A",
    "update_message": "Enter update message here.",
}

update_example_payload = {
    "kind": "retraction",
    "date": "2025-01-13 16:55:08.844845",
    "email": "john.smith@email.com",
    "internal_id": "38249195",
}

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Define the IP address you want to send the request to
ip_address = "142.157.211.4:8000"
# Define the endpoint or URL path
endpoint = "/voe"

# Construct the full URL
url = f"http://{ip_address}{endpoint}"

# Send a POST request
response = requests.post(url, data=detection_example_payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print("It worked!", response.text)
else:
    # Print an error message
    print(f"Error: {response.status_code}")
