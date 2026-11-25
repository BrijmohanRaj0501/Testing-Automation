'''def test_book():
    print("booking executing....")

def test_payment():
    print("payment executing....")

def test_add_to_cart():
    print("add to cart executing....")'''
from asyncio import exceptions

#-----------------------------------------------------------------------------

# by using raise execution

'''def test_book():
    print("booking executing....")

def test_payment():  # tests case failed
    raise Exception

def test_add_to_cart():
    print("add to cart executing....")'''

#---------------------------------------------------------------------------

# by using assert
'''def test_sum1():
    assert 10+20==30,'Not the  sum'

def test_sum2():
    assert 100-10==50,'Not the difference'''

# collected 2 items

# test_file2.py::test_sum1 PASSED
# test_file2.py::test_sum2 FAILED

#-----------------------------------------------------------------------------

'''def test_login():
    print("login executing....")
    def test_logout():
        print('logout executing....')'''

#collected 1 item

# test_file2.py::test_login login executing....
# PASSED

## IN CASE OF nested function , it will execute only outer function.

#--------------------------------------------------------------------------

'''def test_add(a,b):
    print(a+b)

test_add(10,20)'''

# collecting ... 30
# collected 1 item

# test_file2.py::test_add ERROR

# in pytest - it will not take any argument.

#------------------------------------------------------------------------------
'''def test_login():
    print("login 1 executing....")

def test_login():
    print("login 2 executing....")

test_login()
'''
## in pytest if two function having same name then , the latest one will execute only.

# collecting ... login 2 executing....
# collected 1 item

# test_file2.py::test_login login 2 executing....
# PASSED

#--------------------------------------------------------------------------------


'''class sample:
    def test_login(self):
        print('login executing...')

    def test_fill_data(self):
        print('filling data...')

    def test_logout(self):
        print('logout executing...')'''
# collected 0 items

# ============== no tests ran in 0.07s  ==============


# class_name should not follow pytest rule.

#----------------------------------------------------------------------------

'''class Test_Sample:
    def test_login(self):
        print('login executing...')

    def test_fill_data(self):
        print('filling data...')

    def test_logout(self):
        print('logout executing...')'''


# collected 3 items

# test_file2.py::Test_Sample::test_login login executing...
# PASSED
# test_file2.py::Test_Sample::test_fill_data filling data...
# PASSED
# test_file2.py::Test_Sample::test_logout logout executing...
# PASSED

#=========================== 3 passed in 0.06s ============================

## class_name should follow pytest rule so if will passed all thew testcase.

#-----------------------------------------------------------------------------

'''class Test_Sample:
    def login(self):
        print('login executing...')
    def logout(self):
        print('logout executing...')'''

# collected 0 items
## function do not follow Pytest rule.

#---------------------------------------------------------------------------

