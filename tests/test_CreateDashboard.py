import commonFuctions

BASE_URL = commonFuctions.base_url


def test_createDashboards():
    """Testing createFolder method"""
    session = commonFuctions.create_session()
    print("In test_createFolder method:", session)
    org_id = "11"
    data = {
        "description": "Traffic patterns and network performance of the infrastructure",
        "title": "Network Traffic Overview"
    }
    resp_post = session.post(f"{BASE_URL}/api/{org_id}/dashboards", json=data)

    assert resp_post.status_code == 200
    print("received success status code and content is:", resp_post.content)


#calls
test_createDashboards()
