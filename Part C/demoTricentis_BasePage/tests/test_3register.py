from demoTricentis_BasePage.Pages.register import RegisterPage
from time import sleep


def test_register(setup_and_teardown):
    register = RegisterPage(setup_and_teardown)
    register.click_register()
    sleep(2)
    register.click_gender()
    register.enter_first_name('Brij')
    register.enter_last_name('Raj')
    register.enter_email('zxcvb@gmail.com')
    register.enter_password('qwert@56')
    register.enter_cnf_pwd('qwert@56')
    register.click_register_btn()
    sleep(2)

