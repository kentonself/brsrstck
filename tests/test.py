import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common import desired_capabilities as DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


USER = os.getenv('BROWSERSTACK_USER')
PASSWORD = os.environ.get('BROWSERSTACK_PASSWORD')

def test_example(selenium):
    '''
    cap = selenium.DesiredCapabilities.copy()
    cap['bstack:options']['maskCommands'] = 'setValues'
    selenium.set_capability('bstack:options', cap['bstack:options'])
    match selenium.name():
     case 'Chrome':
    if(selenium instanceof ChromeDriver):
        #options = selenium.ChromeOptions()
        cap = selenium.CHROME.copy()
        cap['bstack:options']['maskCommands'] = 'setValues'
        selenium = webdriver.Remote(options = options, desired_capabilities=cap)
    # case 'Firefox':
    else if(selenium instanceof FirefoxDriver):
        #options = selenium.FirefoxOptions()
        cap = selenium.FIREFOX.copy() 
        cap['bstack:options']['maskCommands'] = 'setValues'
        selenium = webdriver.Remote(options = options, desired_capabilities=cap)
    # case 'WebKitGTK':
    else if(selenium instanceof WebKitGTKDriver):
       # options = selenium.WebKitGTKoptions()
        cap = selenium.WEBKITGTK.copy() 
        cap['bstack:options']['maskCommands'] = 'setValues'
        selenium = webdriver.Remote(options = options, desired_capabilities=cap)
    else:
        selenium.execute_script('browserstack_executor: {"action": "annotate", "arguments": {"data":"browserName "' + json.dumps.selenium.capabilities['browserName'] + ' has not been coded, "level": "error"}}')
        '''
    details = selenium.execute_script('browserstack_executor: {"action": "getSessionDetails"}')

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

    invite_link = selenium.find_element(By.ID, 'invite-link').get_attribute('href')

    assert invite_link is not None

    signout = selenium.find_element(By.ID, 'sign_out_link').click

