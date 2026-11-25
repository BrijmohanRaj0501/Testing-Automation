from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait= WebDriverWait(driver, 10)

    def click(self,locator):
        self.driver.find_element(*locator).click()

    def send_keys(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)


    def select_option(self,locator,value):
        dropdown1=self.wait.until(EC.element_to_be_clickable(locator))
        dropdown = Select(dropdown1)
        dropdown.select_by_visible_text(value)

