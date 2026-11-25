import pytest


#wrt to function

''''@pytest.fixture(autouse=True)
def startup():
    print('start')
    yield
    print('End')
'''


# collected 6 items
#
# test_1.py::test_fun1 start
# function_1 executing...
# PASSEDEnd
#
# test_1.py::test_fun2 start
# function_2 executing...
# PASSEDEnd
#
# test_2.py::test_fun3 start
# function_3 executing...
# PASSEDEnd
#
# test_2.py::test_fun4 start
# function_4 executing...
# PASSEDEnd
#
# test_3.py::test_fun5 start
# function5 executing...
# PASSEDEnd
#
# test_3.py::test_fun6 start
# function6 executing...
# PASSEDEnd

# ================================= 6 passed in 0.07s =========================================

#----------------------------------------------------------------------------------------------

#with respect to class

'''@pytest.fixture(autouse=True, scope='class')
def startup():
    print('start')
    yield
    print('End')'''

# collected 6 items
#
# test_1.py::Test1::test_fun1 start
# function_1 executing...
# PASSED
# test_1.py::Test1::test_fun2 function_2 executing...
# PASSEDEnd
#
# test_2.py::Test2::test_fun3 start
# function_3 executing...
# PASSED
# test_2.py::Test2::test_fun4 function_4 executing...
# PASSEDEnd
#
# test_3.py::Test3::test_fun5 start
# function5 executing...
# PASSED
# test_3.py::Test3::test_fun6 function6 executing...
# PASSEDEnd

# ========================== 6 passed in 0.09s ======================================

# with respect to module

'''@pytest.fixture(autouse=True, scope='module')
def startup():
    print('start')
    yield
    print('End')
'''
# collected 6 items
# test_1.py::Test1::test_fun1 start
# function_1 executing...
# PASSED
# test_1.py::Test1::test_fun2 function_2 executing...
# PASSEDEnd
#
# test_2.py::Test2::test_fun3 start
# function_3 executing...
# PASSED
# test_2.py::Test2::test_fun4 function_4 executing...
# PASSEDEnd
#
# test_3.py::Test3::test_fun5 start
# function5 executing...
# PASSED
# test_3.py::Test3::test_fun6 function6 executing...
# PASSEDEnd

# ============================ 6 passed in 0.07s ==========================================
#-------------------------------------------------------------------------------------------

# wrt session

@pytest.fixture(autouse=True, scope='session')
def startup():
    print('start')
    yield
    print('End')

# collected 6 items
#
# test_1.py::Test1::test_fun1 start
# function_1 executing...
# PASSED
# test_1.py::Test1::test_fun2 function_2 executing...
# PASSED
# test_2.py::Test2::test_fun3 function_3 executing...
# PASSED
# test_2.py::Test2::test_fun4 function_4 executing...
# PASSED
# test_3.py::Test3::test_fun5 function5 executing...
# PASSED
# test_3.py::Test3::test_fun6 function6 executing...
# PASSEDEnd

# ========================= 6 passed in 0.07s =========================================