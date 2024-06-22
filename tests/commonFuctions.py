import requests
import os

base_url = os.environ["ZO_BASE_URL"]
username = os.environ["ZO_ROOT_USER_EMAIL"]
password = os.environ["ZO_ROOT_USER_PASSWORD"]


def create_session():
    session = requests.Session()
    resp = session.post(f"{base_url}/auth/login", json={"name": username, "password": password})
    print(resp.status_code)
    if resp.status_code != 200:
        raise Exception("Invalid username/password")
    return session
