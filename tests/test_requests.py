import requests


def test_status():
    r = requests.get("https://gorest.co.in/")
    assert r.status_code == 200


def test_list_users():
    r = requests.get("https://gorest.co.in/public/v2/users")
    assert r.status_code == 200