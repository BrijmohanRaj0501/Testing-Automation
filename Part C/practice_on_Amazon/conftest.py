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

    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    yield driver
    driver.quit()

