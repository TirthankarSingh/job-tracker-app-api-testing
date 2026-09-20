import requests

def test_verify_public_status_endpoint():

    """
    Example response:{
    "app_name": "SuperSQA Job Tracker",
    "api_version": "v1",
    "environment": "local",
    "server_time": "2026-09-20T18:24:13.277007Z"
    }
    """

    url =  'http://localhost:3050/api/v1/public/status'
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    body = response.json()
    body.keys() == ["app_name", "api_version", "environment", "server_time"]
    assert body["app_name"] == "SuperSQA Job Tracker"
    assert body["api_version"] == "v1"
    assert body["environment"] == "local"
    assert body["server_time"] is not None
