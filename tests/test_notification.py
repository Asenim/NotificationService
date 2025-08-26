import requests


BASE_URL = "http://localhost:8080"


# def test_get_notifications():
#
#     tokens = requests.post(
#         url=BASE_URL + "/auth/login",
#         json={"username": "alfob"}
#     )
#
#     access_token = tokens.json()["access"]
#     headers = {"Authorization": f"Bearer {access_token}"}
#
#     response = requests.get(
#         BASE_URL + "/notifications",
#         headers=headers
#     )
#     print(response.json())
#
#
# def test_create_notification():
#     tokens = requests.post(
#         url=BASE_URL + "/auth/login",
#         json={"username": "alfob"}
#     )
#
#     access_token = tokens.json()["access"]
#     headers = {"Authorization": f"Bearer {access_token}"}
#
#     response = requests.post(
#         url=BASE_URL + "/notifications",
#         headers=headers,
#         json={
#             "notification_type": "like",
#             "text": "string"
#         },
#     )
#     print(response.json(), response.status_code, response.text)


# def test_user_register():
#     pass
#
#
# def test_user_login():
#     pass

#
# def test_delete_notification():
#     tokens = requests.post(
#             url=BASE_URL + "/auth/login",
#             json={"username": "alfob"}
#         )
#
#     access_token = tokens.json()["access"]
#     headers = {"Authorization": f"Bearer {access_token}"}
#
#     response = requests.delete(
#         url=BASE_URL + "/notifications/3",
#         headers=headers,
#     )
#     print(response.text)
