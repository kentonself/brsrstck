"""PyTest BrowserStack code to log into BrowserStack itself """
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


USER = os.getenv('BSTACK_USER')
PASSWORD = os.environ.get('BSTACK_PASSWORD')

def test_example(selenium):
    """Test to log into the BrowserStack platform """
    selenium.get('https://automate.browserstack.com/')
    selenium.implicitly_wait(10)

    try:
        # Look for cookie popup and click accept if present
        selenium.find_element(By.ID, 'accept-cookie-notification').click()
    except NoSuchElementException:
        # Popup not present
        pass

    user = selenium.find_element(By.ID, 'user_email_login')
    password = selenium.find_element(By.ID, 'user_password' )
    user.send_keys(USER)
    password.send_keys(PASSWORD)

    selenium.find_element(By.ID, 'user_submit').click()

    try:
        selenium.find_element(By.ID, 'invite-link').get_attribute('href')
    except NoSuchElementException:
        pytest.fail('could not find invite-link')

    selenium.get('https://www.browserstack.com/users/sign_out')
