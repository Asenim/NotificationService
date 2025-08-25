import requests


BASE_URL = "http://localhost:8080"


def test_get_notifications():

    tokens = requests.post(
        url=BASE_URL + "/auth/login",
        json={"username": "alfob"}
    )

    access_token = tokens.json()["access"]
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(
        BASE_URL + "/notifications",
        headers=headers
    )
    print(response.json())


def test_create_notification():
    tokens = requests.post(
        url=BASE_URL + "/auth/login",
        json={"username": "alfob"}
    )

    access_token = tokens.json()["access"]
    headers = {"Authorization": f"Bearer {access_token}"}

    info = requests.post(
        url=BASE_URL + "/notifications",
        headers=headers,
    )
    print(info.json())
