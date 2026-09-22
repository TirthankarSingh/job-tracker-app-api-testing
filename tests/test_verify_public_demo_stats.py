import requests
import os

def test_verify_public_demo_stats():

    """
    response example:{
    "total_seeded_applications": 4,
    "status_counts": {
        "potential": 2,
        "applied": 1,
        "in_progress": 1,
        "final_stage": 0,
        "hired": 0,
        "rejected": 0,
        "withdrawn": 0,
        "total": 4
    }
        }
    """
    url = os.getenv("BASE_URL") + "/api/v1/public/demo-stats"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    body = response.json()
    # breakpoint()
    body.keys() == ["total_seeded_applications", "status_counts"]

    #verify the total_seeded_applications is an integer and the status_counts is a dictionary
    assert isinstance(body["total_seeded_applications"], int)
    assert isinstance(body["status_counts"], dict)

    status_counts = body["status_counts"]
    #verify the status counts are integers
    for status, count in status_counts.items():
        print(f"key: {status}, value: {count}")
        assert isinstance(count, int), f"Expected count to be an integer, but got {type(count)}"