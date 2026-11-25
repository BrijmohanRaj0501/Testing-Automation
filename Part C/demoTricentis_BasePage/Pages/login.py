from selenium.webdriver.common.by import By
from demoTricentis_BasePage.Pages.basepage import BasePage

class LoginPage(BasePage):
    login_link = (By.XPATH, '//a[text()="Log in"]')
    email = (By.ID,'Email')
    password = (By.ID,'Password')
    login_button = (By.XPATH, '//input[@class="button-1 login-button"]')

    def click_login_link(self):
        self.click(self.login_link)

    def enter_email(self,email_text):
        self.enter_text(self.email,email_text)

    def enter_password(self,password_text):
        self.enter_text(self.password,password_text)

    def click_login_button(self):
        self.click(self.login_button)
