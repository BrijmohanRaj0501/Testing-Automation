'''import pytest

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
'''

# cross-Browser Testing =

import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def setup_and_teardown(request):

    parameter=request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()

    if parameter == 'firefox':
        driver = webdriver.Firefox()

    if parameter == 'edge':
        driver = webdriver.Edge()

    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()


