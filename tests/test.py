import os
import pytest
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities as DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


USER = os.getenv('BSTACK_USER')
PASSWORD = os.environ.get('BSTACK_PASSWORD')

def test_example(selenium):
    selenium.get('https://automate.browserstack.com/')
    selenium.implicitly_wait(10)

    try:
        # Look for cookie popup and click accept if present
        cookie = selenium.find_element(By.ID, 'accept-cookie-notification').click()
    except NoSuchElementException:
        # Popup not present
        pass

    user = selenium.find_element(By.ID, 'user_email_login')
    password = selenium.find_element(By.ID, 'user_password' )
    user.send_keys(USER)
    password.send_keys(PASSWORD)

    selenium.find_element(By.ID, 'user_submit').click()

    try:
        invite_link = selenium.find_element(By.ID, 'invite-link').get_attribute('href')
    except NoSuchElementException:
        pytest.fail('could not find invite-link')

    selenium.get('https://www.browserstack.com/users/sign_out')
