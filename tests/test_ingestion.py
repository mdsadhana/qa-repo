import json

import commonFuctions

BASE_URL = commonFuctions.BASE_URL


def test_ingestion():
    """Search logs if it exists"""
    session = commonFuctions.create_session()
    print("In test_ingestion method:")
    org_id = "11"
    stream_name = "aa11"
    data = [
        {
            "Athlete": "Alfred",
            "City": "Athens",
            "Country": "HUN",
            "Discipline": "Swimming",
            "Sport": "Aquatics",
            "Year": 1896
        },
        {
            "Athlete": "HERSCHMANN",
            "City": "Athens",
            "Country": "CHN",
            "Discipline": "Swimming",
            "Sport": "Aquatics",
            "Year": 1896
        }
    ]
    resp_post = session.post(f"{BASE_URL}/api/{org_id}/{stream_name}/_json", json=data)
    json_str = json.dumps(resp_post.json(), indent=4)
    assert resp_post.status_code == 200
    print("received success status code and content is:", json_str)


