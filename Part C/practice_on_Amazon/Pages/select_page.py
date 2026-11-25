from selenium.webdriver.common.by import By
from practice_on_Amazon.Pages.basepage import BasePage

class SelectPage(BasePage):
    sort_Dropdown =(By.ID,'s-result-sort-select')

    def select_sort_option(self,option):
        self.select_option(self.sort_Dropdown,option)
