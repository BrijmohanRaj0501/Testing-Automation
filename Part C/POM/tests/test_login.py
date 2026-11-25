import pytest
from POM.Pages.login import LoginPage
from POM.utilities.read_login_data import get_login_data
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

@pytest.mark.parametrize("username,password",get_login_data())
def test_valid_login(username,password):
    driver=Chrome(options=o)
    driver.get('https://www.saucedemo.com/')
    sleep(1)
    login =LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    sleep(1)
    assert 'inventory' in driver.current_url,'login failed...'










'''
from POM.Pages.login import Search
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

def test_search_field():
    driver=Chrome(options=o)
    driver.get('https://www.amazon.in/')
    sleep(1)
    driver.maximize_window()
    amazon =Search(driver)
    amazon.search_product('Mobiles')
    amazon.click_search()
    sleep(1)
    driver.execute_script("window.scrollBy(0,400)")
'''