import json

import commonFuctions

BASE_URL = commonFuctions.BASE_URL


def test_get():
    """Testing get method"""
    session = commonFuctions.create_session()
    print("In get method:", session)
    resp_get = session.get(f"{BASE_URL}/api/organizations")
    json_str = json.dumps(resp_get.json(), indent=4)
    assert resp_get.status_code == 200
    print("received success status code and content is:", json_str)


#calls
test_get()
