from models import BasePage


def test_login():
    login_result = BasePage.login("secret_sauce", "secret_sauce")
    assert login_result == "Login ok"
