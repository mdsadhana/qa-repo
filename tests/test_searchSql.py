import json

import commonFuctions
import test_ingestion
BASE_URL = commonFuctions.base_url


def test_searchSql():
    test_ingestion.test_ingestion()
    session = commonFuctions.create_session()
    print("In test_searchSql method:")
    org_id = "11"
    data = {
        "aggs": {
            "histogram": "select histogram(_timestamp, '30 second') AS zo_sql_key, count(*) AS zo_sql_num from query GROUP BY zo_sql_key ORDER BY zo_sql_key"
        },
        "query": {
            "end_time": 1675185660872049,
            "from": 0,
            "size": 10,
            "sql": "select * from k8s ",
            "start_time": 1675182660872049
        }
    }
    resp_post = session.post(f"{BASE_URL}/api/{org_id}/_search", json=data)
    json_str = json.dumps(resp_post.json(), indent=4)
    assert resp_post.status_code == 200
    print("received success status code and content is:", json_str)


#call
test_searchSql()