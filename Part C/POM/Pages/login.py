from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID,'user-name')
    password = (By.ID,'password')
    login_btn = (By.ID,'login-button')


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()














'''class Search:
    product_name=(By.ID,'twotabsearchtextbox')
    search_icon=(By.ID,'nav-search-submit-button')

    def __init__(self,driver):
        self.driver = driver

    def search_product(self,product):
        self.driver.find_element(*self.product_name).send_keys(product)

    def click_search(self):
        self.driver.find_element(*self.search_icon).click()'''











