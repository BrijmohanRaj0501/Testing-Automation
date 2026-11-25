import pytest

'''@pytest.mark.execute_now
def test_login():
    print('login executing.....')

def test_add_to_cart():
    print('add cart executing.....')
@pytest.mark.execute_now
def test_logout():
    print('logout executing.....')'''

# collected 3 items / 1 deselected / 2 selected
#
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_logout logout executing.....
# PASSED


'''@pytest.mark.smoke
def test_1():
    print('1 executing.....')

@pytest.mark.smoke
@pytest.mark.regression
def test_2():
    print('2 executing.....')

def test_3():
    print('3 executing.....')

@pytest.mark.regression
def test_4():
    print('4 executing.....')

@pytest.mark.functional
def test_5():
    print('5 executing.....')'''
#---------------------------------------------------------------------
# py -m pytest -vs .\test_markers.py -m "smoke or regression"
# 'result->'
# collected 5 items / 2 deselected / 3 selected
#
# test_markers.py::test_1 1 executing.....
# PASSED
# test_markers.py::test_2 2 executing.....
# PASSED
# test_markers.py::test_4 4 executing.....
# PASSED
#----------------------------------------------------------------------------
# py -m pytest -vs .\test_markers.py -m "regression"
# 'result-->'
# collected 5 items / 3 deselected / 2 selected
#
# test_markers.py::test_2 2 executing.....
# PASSED
# test_markers.py::test_4 4 executing.....
# PASSED
#------------------------------------------------------------------------------
# py -m pytest -vs .\test_markers.py -m "smoke"
# 'result ->'
# collected 5 items / 3 deselected / 2 selected
#
# test_markers.py::test_1 1 executing.....
# PASSED
# test_markers.py::test_2 2 executing.....
# PASSED
#---------------------------------------------------------------------------------

'''class Test_calculator:
    @pytest.mark.smoke
    def test_addition(self):
        assert 10+12==22,'addition error'
    @pytest.mark.regression
    def test_subtraction(self):
        assert 50-35==15,'subtraction error'
    @pytest.mark.smoke
    def test_multiplication(self):
        assert 5*3==30,'multiplication error'
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_division(self):
        assert 50/5==10,'division error'
    @pytest.mark.sanity
    def test_modulus(self):
        assert 5%3==2,'modulus error'
    @pytest.mark.regression
    def test_square(self):
        assert 5**2==25,'square error'
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_cube(self):
        assert 5**3==125,'cube error'

    def test_floor_division(self):
        assert 5//3==1,'floor division error'''

#-------------------------------------------------------------------------
# #1) Run only smoke tests
# collected 8 items / 4 deselected / 4 selected
#
# test_markers.py::Test_calculator::test_addition PASSED
# test_markers.py::Test_calculator::test_multiplication FAILED
# test_markers.py::Test_calculator::test_division PASSED
# test_markers.py::Test_calculator::test_cube PASSED
#-------------------------------------------------------------------------
# 2) Run regression tests
# collected 8 items / 4 deselected / 4 selected
#
# test_markers.py::Test_calculator::test_subtraction PASSED
# test_markers.py::Test_calculator::test_division PASSED
# test_markers.py::Test_calculator::test_square PASSED
# test_markers.py::Test_calculator::test_cube PASSED
#------------------------------------------------------------------------------
# 3) Run only sanity tests
# collected 8 items / 6 deselected / 2 selected
#
# test_markers.py::Test_calculator::test_modulus PASSED
# test_markers.py::Test_calculator::test_cube PASSED
#------------------------------------------------------------------------------
# 4) Run all the tests methods
# collected 8 items
#
# test_markers.py::Test_calculator::test_addition PASSED
# test_markers.py::Test_calculator::test_subtraction PASSED
# test_markers.py::Test_calculator::test_multiplication FAILED
# test_markers.py::Test_calculator::test_division PASSED
# test_markers.py::Test_calculator::test_modulus PASSED
# test_markers.py::Test_calculator::test_square PASSED
# test_markers.py::Test_calculator::test_cube PASSED
# test_markers.py::Test_calculator::test_floor_division PASSED
#------------------------------------------------------------------------------
# 5) Run tests having both smoke and regression
# collected 8 items / 6 deselected / 2 selected
#
# test_markers.py::Test_calculator::test_modulus PASSED
# test_markers.py::Test_calculator::test_cube PASSED
#----------------------------------------------------------------------------
# 6) Run tests having both smoke and sanity
# collected 8 items / 7 deselected / 1 selected
#
# test_markers.py::Test_calculator::test_cube PASSED
#---------------------------------------------------------------------------
# 7) Run all tests methods except regression
# collected 8 items / 4 deselected / 4 selected
#
# test_markers.py::Test_calculator::test_addition PASSED
# test_markers.py::Test_calculator::test_multiplication FAILED
# test_markers.py::Test_calculator::test_modulus PASSED
# test_markers.py::Test_calculator::test_floor_division PASSED
#----------------------------------------------------------------------------


'''def test_login():
    print('login executing.....')
def test_add_to_cart():
    print('add cart executing.....')
@pytest.mark.skip
def test_logout():
    print('logout executing.....')'''
#---------------------------------------------------------------------------
    # collected 3 items
    #
    # test_markers.py::test_login login executing.....
    # PASSED
    # test_markers.py::test_add_to_cart add cart executing.....
    # PASSED
    # test_markers.py::test_logout SKIPPED (unconditional skip)
    #
    # =============== 2 passed, 1 skipped in 0.10s ===============
#------------------------------------------------------------------------------
'''def test_login():
    print('login executing.....')
def test_add_to_cart():
    print('add cart executing.....')
@pytest.mark.skip(reason='skip it because it does not required')
def test_logout():
    print('logout executing.....')'''
#---------------------------------------------------------------------
# collected 3 items
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart add cart executing.....
# PASSED
# test_markers.py::test_logout SKIPPED (skip it because it does not required)
#
# ====================== 2 passed, 1 skipped in 0.10s ===================
#----------------------------------------------------------------------------
'''@pytest.mark.skip  # it will skip the whole class
class Testsample:
    def test_login(self):
        print('login executing.....')

    def test_add_to_cart(self):
        print('add cart executing.....')

    def test_logout(self):
        print('logout executing.....')'''

#--------------------------------------------------------------------------
# collected 3 items
#
# test_markers.py::Testsample::test_login SKIPPED (unconditional skip)
# test_markers.py::Testsample::test_add_to_cart SKIPPED (unconditional skip)
# test_markers.py::Testsample::test_logout SKIPPED (unconditional skip)
#----------------------------------------------------------------------------
# with True Condition
'''def test_login():
    print('login executing.....')

@pytest.mark.skipif(True, reason='skip it because it does not required')
def test_add_to_cart():
    print('add cart executing.....')

def test_logout():
    print('logout executing.....')'''

# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart SKIPPED (skip it because it does not required)
# test_markers.py::test_logout logout executing.....
# PASSED
#
# ================= 2 passed, 1 skipped in 0.06s ====================

#-------------------------------------------------------------------------
#with False Condition

'''def test_login():
    print('login executing.....')

@pytest.mark.skipif(False, reason='skip it because it does not required')
def test_add_to_cart():
    print('add cart executing.....')

def test_logout():
    print('logout executing.....')'''

#
# collected 3 items
#
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart add cart executing.....
# PASSED
# test_markers.py::test_logout logout executing.....
# PASSED
# ============================ 3 passed in 0.06s ==========================

#-------------------------------------------------------------------

# xfail
# with passed testcases
'''def test_login():
    print('login executing.....')

@pytest.mark.xfail
def test_add_to_cart():
    print('add cart executing.....')

def test_logout():
    print('logout executing.....')'''


# collected 3 items
#
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart add cart executing.....
# XPASS
# test_markers.py::test_logout logout executing.....
# PASSED

#================= 2 passed, 1 xpassed in 0.06s ==================
# with failed testcases
'''def test_login():
    print('login executing.....')

@pytest.mark.xfail
def test_add_to_cart():
    raise Exception

def test_logout():
    print('logout executing.....')'''

# collected 3 items
#
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart XFAIL
# test_markers.py::test_logout logout executing.....
# PASSED

#================= 2 passed, 1 xfailed in 0.13s ===================
#---------------------------------------------------------------------------


# paramterized ->

'''@pytest.mark.parametrize("a,b",[(10,20),(30,50),(30,10)])
def test_add(a,b):
    print(a+b)'''

# collected 3 items
#
# test_markers.py::test_add[10-20] 30
# PASSED
# test_markers.py::test_add[30-50] 80
# PASSED
# test_markers.py::test_add[30-10] 40
# PASSED
#
# ======================== 3 passed in 0.11s ======================

#-----------------------------------------------------------------------------

'''@pytest.mark.parametrize("u,p",[('standard_user','secret_sauce'),('locked_out_user','secret_sauce'),('problem_user','secret_sauce'),('error_user','secret_sauce')])
def test_login(u,p):
    print("login_id:",u,"password:", p )'''


# collected 4 items
#
# test_markers.py::test_login[standard_user-secret_sauce] login_id: standard_user password: secret_sauce
# PASSED
# test_markers.py::test_login[locked_out_user-secret_sauce] login_id: locked_out_user password: secret_sauce
# PASSED
# test_markers.py::test_login[problem_user-secret_sauce] login_id: problem_user password: secret_sauce
# PASSED
# test_markers.py::test_login[error_user-secret_sauce] login_id: error_user password: secret_sauce

#================================================= 3 passed in 0.11s ============================================

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

@pytest.mark.parametrize("u,p",[('standard_user','secret_sauce'),('locked_out_user','secret_sauce'),('problem_user','secret_sauce'),('error_user','secret_sauce'),('visual_user','secret_sauce'),('performance_glitch_user','secret_sauce')])
def test_login(u,p):
    driver.get('https://www.saucedemo.com/')
    sleep(1)
    driver.find_element(By.ID, 'user-name').send_keys(u)
    driver.find_element(By.ID, 'password').send_keys(p)
    driver.find_element(By.ID, 'login-button').click()
    sleep(2)
    assert "inventory" in driver.current_url,'login failed....'

# collected 6 items
#
# test_markers.py::test_login[standard_user-secret_sauce] PASSED
# test_markers.py::test_login[locked_out_user-secret_sauce] FAILED
# test_markers.py::test_login[problem_user-secret_sauce] PASSED
# test_markers.py::test_login[error_user-secret_sauce] PASSED
# test_markers.py::test_login[visual_user-secret_sauce] PASSED
# test_markers.py::test_login[performance_glitch_user-secret_sauce] PASSED

# ======================= 1 failed, 5 passed in 30.16s ========================
#------------------------------------------------------------------------------------

'''@pytest.mark.parametrize("u,p",[('asdfg@gmail.com','asdfg@01'),('zxcvg@gmail.com','zxcvbg@01'),('qwert@gmail.com','qwert@01')])
def test_login(u,p):
    driver.get('https://demowebshop.tricentis.com/login')
    sleep(1)
    driver.find_element(By.ID, 'Email').send_keys(u)
    driver.find_element(By.ID, 'Password').send_keys(p)
    driver.find_element(By.XPATH, '//input[@class="button-1 login-button"]').click()
    sleep(2)'''

#---------------------------------------------------------------------------------------------------------------------------


#pytest-dependency

'''@pytest.mark.dependency()
def test_login():
    print("login executing.....")

@pytest.mark.dependency(depends=['test_login'])
def test_add_to_cart():
    print("add cart executing.....")
'''
# collected 2 items
#
# test_markers.py::test_login login executing.....
# PASSED
# test_markers.py::test_add_to_cart add cart executing.....
# PASSED
#
# =========================== 2 passed in 0.06s ===================

'''@pytest.mark.dependency()
def test_login():
    raise Exception

@pytest.mark.dependency(depends=['test_login'])
def test_add_to_cart():
    print("add cart executing.....")'''


# collected 2 items
#
# test_markers.py::test_login FAILED
# test_markers.py::test_add_to_cart SKIPPED (test_add_to_cart depends on test_login)

# =========================== 1 failed, 1 skipped in 0.18s ========================

'''@pytest.mark.dependency()
def test_login():
    print("logout executing.....")

@pytest.mark.dependency(depends=['test_login'])
def test_dashboard():
    print("dashboard executing.....")

@pytest.mark.dependency(depends=['test_dashboard'])
def test_profile():
    print("profile executing.....")
'''
# collected 3 items
#
# test_markers.py::test_login logout executing.....
# PASSED
# test_markers.py::test_dashboard dashboard executing.....
# PASSED
# test_markers.py::test_profile profile executing.....
# PASSED
#
# ===================== 3 passed in 0.11s ============


'''@pytest.mark.dependency()
def test_login():
    print("logout executing.....")

@pytest.mark.dependency(depends=['test_login'])
def test_dashboard():
    raise Exception

@pytest.mark.dependency(depends=['test_dashboard'])
def test_profile():
    print("profile executing.....")'''

# collected 3 items
#
# test_markers.py::test_login logout executing.....
# PASSED
# test_markers.py::test_dashboard FAILED
# test_markers.py::test_profile SKIPPED (test_profile depends on test_dashboard)
#
# =================== 1 failed, 1 passed, 1 skipped in 0.32s =======================












