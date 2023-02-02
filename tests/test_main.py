from models import BasePage


def test_browser():
    BasePage.open_page()
    BasePage.tear_down()
    assert True




