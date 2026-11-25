# question 1

'''def test_mark_attendance():
    print('attendance mark sucessfully')

def test_view_attendance():
    print('attendance details displayed sucessfully')'''

# collected 2 items

# practice.py::test_mark_attendance attendance mark sucessfully
# PASSED
# practice.py::test_view_attendance attendance details displayed sucessfully
# PASSED

#----------------------------------------------------------------------
# question 2
'''class Test_Sample:
    def test_create_account(self):
        print('account created sucessfully')
    def open_account(self):
        print('account opened')
    def test_update_profile(self):
        print('profile updated sucessfully')
    def close_account(self):
        print('account closed')'''

# collected 2 items
#
# practice.py::Test_Sample::test_create_account account created sucessfully
# PASSED
# practice.py::Test_Sample::test_update_profile profile updated sucessfully
# PASSED

#----------------------------------------------------------------------------------
# question 3

'''class Test_Sample:
    def test_search_product(self):
        print('product search started')
        raise Exception
    def test_view_product(self):
        print('product details displayed')
    def test_add_wishlist(self):
        print('product added to wishlist ')'''

#collected 3 items

# practice.py::Test_Sample::test_search_product product search started
# FAILED
# practice.py::Test_Sample::test_view_product product details displayed
# PASSED
# practice.py::Test_Sample::test_add_wishlist product added to wishlist
# PASSED

#---------------------------------------------------------------------------------

# question 4


from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://www.saucedemo.com/')
sleep(2)
class Test_Application:
    def test_username(self):
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        sleep(1)

    def test_password(self):
        driver.find_element(By.ID,'password').send_keys('secret_sauce')

    def test_login(self):
        driver.find_element(By.ID,'login-button').click()

