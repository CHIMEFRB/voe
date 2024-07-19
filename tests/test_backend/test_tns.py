from frbvoe.backend.tns import TNS

def test_submit_frb_to_sandbox_tns():
    tns = TNS()
    frb_data = {
        "name": "12345678",
        "ra": "12:34:56.789",
        "dec": "+12:34:56.789",
        "redshift": 0.5
    }
    response = tns.submit(frb_data, sandbox=True)
    assert response.status_code == 200
    assert response.json() == {"message": "FRB submitted to sandbox TNS."}

def test_submit_frb_with_custom_period():
    tns = TNS()
    frb_data = {
        "name": "FRB2022",
        "ra": "12:34:56.789",
        "dec": "+12:34:56.789",
        "redshift": 0.5
    }
    response = tns.submit(frb_data, proprietary_period=30)
    assert response.status_code == 200
    assert response.json() == {"message": "FRB submitted successfully with custom period."}

def test_submit_frb_with_invalid_data():
    tns = TNS()
    frb_data = {
        "name": "FRB2022",
        "ra": "12:34:56.789",
        "dec": "+12:34:56.789",
        "redshift": "invalid"
    }
    response = tns.submit(frb_data)
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid data provided."}