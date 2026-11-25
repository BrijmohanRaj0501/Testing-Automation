from selenium.webdriver.common.by import By
from practice_on_Amazon.Pages.basepage import BasePage

class SearchPage(BasePage):
    search_field = (By.ID, 'twotabsearchtextbox')
    search_button = (By.ID,'nav-search-submit-button')

    def search_product(self,product):
        self.send_keys(self.search_field,product)
        self.click(self.search_button)
