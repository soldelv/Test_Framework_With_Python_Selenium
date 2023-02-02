from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)


def open_page():
    driver.get('https://www.saucedemo.com/')


def tear_down():
    driver.close()
    driver.quit()


def logout():
    print("to do")


def login(user, password):
    open_page()

    # Fill login form
    user_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    user_field.send_keys(user)
    password_field.send_keys(password)
    login_button = driver.find_element(By.NAME, "login-button")
    wait.until(EC.element_to_be_clickable(login_button))
    login_button.click()

    return "Login ok"


def check_login_fail():
    fail_message = "to do"
    return fail_message
