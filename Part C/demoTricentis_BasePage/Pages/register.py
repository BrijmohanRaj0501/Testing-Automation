from selenium.webdriver.common.by import By
from demoTricentis_BasePage.Pages.basepage import BasePage

class RegisterPage(BasePage):
    Register_link =(By.XPATH, '//a[text()="Register"]')
    gender = (By.ID,'gender-male')
    first_name = (By.ID,'FirstName')
    last_name = (By.ID,'LastName')
    email = (By.ID,'Email')
    password = (By.ID,'Password')
    cnf_pwd=(By.ID,'ConfirmPassword')
    register_btn = (By.ID, 'register-button')

    def click_register(self):
        self.click(self.Register_link)
    def click_gender(self):
        self.click(self.gender)
    def enter_first_name(self,first_name_txt):
        self.enter_text(self.first_name,first_name_txt)
    def enter_last_name(self,last_name_txt):
        self.enter_text(self.last_name,last_name_txt)
    def enter_email(self,email_id_txt):
        self.enter_text(self.email,email_id_txt)
    def enter_password(self,password_txt):
        self.enter_text(self.password,password_txt)
    def enter_cnf_pwd(self,cnf_pwd_txt):
        self.enter_text(self.cnf_pwd,cnf_pwd_txt)
    def click_register_btn(self):
        self.click(self.register_btn)
