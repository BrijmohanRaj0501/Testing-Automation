'''def test_login():
    print('login executing...')

def test_fill_data():
    print('filling data...')

def test_logout():
    print('logout executing...')'''

#test_login()
#test_fill_data()
#test_logout()

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://demowebshop.tricentis.com/')
sleep(2)
class Test_Application:
    def test_click_Register(self):
        driver.find_element(By.XPATH,'//a[text()="Register"]').click()
        sleep(2)

    def test_fill_gender(self):
        driver.find_element(By.ID,'gender-male').click()
        sleep(1)

    def test_first_name(self):
        driver.find_element(By.ID,'FirstName').send_keys('Brijmohan')
        sleep(1)

    def test_last_name(self):
        driver.find_element(By.ID,'LastName').send_keys('Sharma')
        sleep(1)

    def test_Email(self):
        driver.find_element(By.ID,'Email').send_keys('brijasdghd@gmail.com')
        sleep(1)

    def test_pass(self):
        driver.find_element(By.ID,'Password').send_keys('Rajsharma#123')
        sleep(1)

    def test_cnf_pass(self):
        driver.find_element(By.ID,'ConfirmPassword').send_keys('Rajsharma#123')
        sleep(1)

    def test_register_btn(self):
        driver.find_element(By.ID,'register-button').click()
        sleep(2)


# collected 8 items
#
# test_file1.py::Test_Application::test_click_Register PASSED
# test_file1.py::Test_Application::test_fill_gender PASSED
# test_file1.py::Test_Application::test_first_name PASSED
# test_file1.py::Test_Application::test_last_name PASSED
# test_file1.py::Test_Application::test_Email PASSED
# test_file1.py::Test_Application::test_pass PASSED
# test_file1.py::Test_Application::test_cnf_pass PASSED
# test_file1.py::Test_Application::test_register_btn PASSED













