'''import pytest

def test_login():
    print('login executing.....')

@pytest.mark.xfail
def test_add_to_cart():
    raise Exception

def test_logout():
    print('logout executing.....')

def test_multiplication():
    assert 5 * 3 == 30, 'multiplication error'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach", True)

def test_amazon():
    driver = Chrome(options=o)

    driver.get('https://www.amazon.in')
    driver.maximize_window()
    sleep(2)
    ele=driver.find_element(By.XPATH,'//a[text()="Mobiles"]')
    action=ActionChains(driver)
    action.click(ele)
    action.perform()
    driver.save_screenshot("proof1.png")



