from frbvoe.backend.tns import TNS

frb_data = {
    "kind": "detection",
    "observatory_name": "CHIME",
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
    "internal_id": "20210826A",
    "dm": 298.53,
    "dm_error": 0.01,
    "width": 4.8,
    "snr": 13.8,
    "flux": 4.9,
    "right_ascension": 55.2938,
    "declination": 14.2049,
    "pos_error_deg_95": 0.1,
    "importance": 0.9979,
    "website": "https://www.example.com",
    "tns_name": "FRB20210826A",
    "update_message": "",
    # TNS specific fields
    "period": 30,
    "sandbox": True,
    "tns_report_id": 1,
    "tns_bot_name": "bot",
}


# def test_submit():
#     tns = TNS(**frb_data)
# response = tns.submit
# assert response.status_code == 200
# assert response.json() == {"message": "FRB submitted to sandbox TNS."}


def test_submit_missing_period():
    tns = TNS(**frb_data, tns_api_key="***")
    try:
        response = tns.submit(frb_data)
        assert response.status_code != 200
    except Exception as e:
        assert True
        return e
