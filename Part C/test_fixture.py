import pytest

'''def test_func1():
    print("good morning")
    print("Function 1 executing ......")
    print("Thank You")

def test_func2():
    print("good morning")
    print("Function 2 executing ......")
    print("Thank You")

def test_func3():
    print("good morning")
    print("Function 3 executing ......")
    print("Thank You")'''


# collected 3 items
#
# test_fixture.py::test_func1 good morning
# Function 1 executing ......
# Thank You
# PASSED
# test_fixture.py::test_func2 good morning
# Function 2 executing ......
# Thank You
# PASSED
# test_fixture.py::test_func3 good morning
# Function 3 executing ......
# Thank You
# PASSED

# ========================= 3 passed in 0.10s ==============================

#------------------------------------------------------------------------------



'''@pytest.fixture
def great():
    print("good morning")

def test_func1(great):
    print("Function 1 executing ......")

def test_func2(great):
    print("Function 2 executing ......")

def test_func3(great):
    print("Function 3 executing ......")'''


# collected 3 items
#
# test_fixture.py::test_func1 good morning
# Function 1 executing ......
# PASSED
# test_fixture.py::test_func2 good morning
# Function 2 executing ......
# PASSED
# test_fixture.py::test_func3 good morning
# Function 3 executing ......
# PASSED

# ================================== 3 passed in 0.06s =====================
#----------------------------------------------------------------------------

'''@pytest.fixture
def great():
    print("good morning")
    yield
    print("Thank You")

def test_func1(great):
    print("Function 1 executing ......")

def test_func2(great):
    print("Function 2 executing ......")

def test_func3(great):
    print("Function 3 executing ......")'''

# collected 3 items
#
# test_fixture.py::test_func1 good morning
# Function 1 executing ......
# PASSEDThank You
#
# test_fixture.py::test_func2 good morning
# Function 2 executing ......
# PASSEDThank You
#
# test_fixture.py::test_func3 good morning
# Function 3 executing ......
# PASSEDThank You
#
#
# ====================== 3 passed in 0.07s ========================

#---------------------------------------------------------------------------
# with autouse

'''@pytest.fixture(autouse=True)
def great():
    print("good morning")
    yield
    print("Thank You")

def test_func1():
    print("Function 1 executing ......")

def test_func2():
    print("Function 2 executing ......")

def test_func3():
    print("Function 3 executing ......")'''

# collected 3 items
#
# test_fixture.py::test_func1 good morning
# Function 1 executing ......
# PASSEDThank You
#
# test_fixture.py::test_func2 good morning
# Function 2 executing ......
# PASSEDThank You
#
# test_fixture.py::test_func3 good morning
# Function 3 executing ......
# PASSEDThank You
#
#
# ================================== 3 passed in 0.07s ================================
#----------------------------------------------------------------------------------------

# with class function
'''@pytest.fixture(autouse=True)
def great():
    print("good morning")
    yield
    print("Thank You")

class TestFix:
    def test_func1(self):
        print("Function 1 executing ......")

    def test_func2(self):
        print("Function 2 executing ......")

    def test_func3(self):
        print("Function 3 executing ......")'''


#-----------------------------------------------------------------------------------
# with scope ="class"
'''@pytest.fixture(autouse=True, scope="class")
def great():
    print("good morning")
    yield
    print("Thank You")

class TestFix:
    def test_func1(self):
        print("Function 1 executing ......")

    def test_func2(self):
        print("Function 2 executing ......")

    def test_func3(self):
        print("Function 3 executing ......")
'''
# collected 3 items
#
# test_fixture.py::TestFix::test_func1 good morning
# Function 1 executing ......
# PASSED
# test_fixture.py::TestFix::test_func2 Function 2 executing ......
# PASSED
# test_fixture.py::TestFix::test_func3 Function 3 executing ......
# PASSEDThank You
#
#
# ========================================= 3 passed in 0.06s ===============================
#--------------------------------------------------------------------------------------------


'''@pytest.fixture(autouse=True, scope="class")
def great():
    print("good morning")
    yield
    print("Thank You")

class TestFix:
    def test_func1(self):
        print("Function 1 executing ......")

    def test_func2(self):
        print("Function 2 executing ......")

    def test_func3(self):
        print("Function 3 executing ......")

class TestFix2:
    def test_func4(self):
        print("Function 4 executing ......")

    def test_func5(self):
        print("Function 5 executing ......")'''

# collected 5 items
# #
# test_fixture.py::TestFix::test_func1 good morning
# Function 1 executing ......
# PASSED
# test_fixture.py::TestFix::test_func2 Function 2 executing ......
# PASSED
# test_fixture.py::TestFix::test_func3 Function 3 executing ......
# PASSEDThank You
#
# test_fixture.py::TestFix2::test_func4 good morning
# Function 4 executing ......
# PASSED
# test_fixture.py::TestFix2::test_func5 Function 5 executing ......
# PASSEDThank You
#
#
# ======================================= 5 passed in 0.06s ==================================
#---------------------------------------------------------------------------------------------
# scope as module

'''@pytest.fixture(autouse=True, scope="module")
def great():
    print("good morning")
    yield
    print("Thank You")

class TestFix:
    def test_func1(self):
        print("Function 1 executing ......")

    def test_func2(self):
        print("Function 2 executing ......")

    def test_func3(self):
        print("Function 3 executing ......")

class TestFix2:
    def test_func4(self):
        print("Function 4 executing ......")

    def test_func5(self):
        print("Function 5 executing ......")

def test_func6():
    print("Function 6 executing ......")'''


# collected 6 items
#
# test_fixture.py::TestFix::test_func1 good morning
# Function 1 executing ......
# PASSED
# test_fixture.py::TestFix::test_func2 Function 2 executing ......
# PASSED
# test_fixture.py::TestFix::test_func3 Function 3 executing ......
# PASSED
# test_fixture.py::TestFix2::test_func4 Function 4 executing ......
# PASSED
# test_fixture.py::TestFix2::test_func5 Function 5 executing ......
# PASSED
# test_fixture.py::test_func6 Function 6 executing ......
# PASSEDThank You


#================================== 6 passed in 0.07s ========================================
#--------------------------------------------------------------------------------------------

# task --01
'''@pytest.fixture(autouse=True)
def setup():
    print("browser opened")

def test_login():
    print("Login executing.....")
'''

# collected 1 item
#
# test_fixture.py::test_login browser opened
# Login executing.....
# PASSED
#
# ==================================== 1 passed in 0.06s ======================


# task--02
'''@pytest.fixture(autouse=True)
def browser():
    print("browser opened")
    yield
    print("browser closed")

def test_google():
    print("google opening.....")

def test_amazon():
    print("amazon opening.....")

def test_myntra():
    print("myntray opening.....")'''

# collected 3 items
# #
# test_fixture.py::test_google browser opened
# google opening.....
# PASSEDbrowser closed
#
# test_fixture.py::test_amazon browser opened
# amazon opening.....
# PASSEDbrowser closed
#
# test_fixture.py::test_myntra browser opened
# myntray opening.....
# PASSEDbrowser closed

# ========================= 3 passed in 0.06s ============================================


