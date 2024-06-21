import requests

BASE_URL = "http://localhost:5080"
username = "root@example.com"
password = "Complexpass#123"

def create_session():
    session = requests.Session()
    resp = session.post(f"{BASE_URL}/auth/login", json={"name": username, "password": password})
    print(resp.status_code)
    if resp.status_code != 200:
        raise Exception("Invalid username/password")
    return session
