import pytest
@pytest.mark.sanity
@pytest.mark.smoke
def test_1():
    print('test_1 executing.....')
@pytest.mark.sanity
def test_2():
    print('test_2 executing.....')
@pytest.mark.smoke
def test_3():
    print('test_3 executing.....')
@pytest.mark.skip(reason="skip because it does not required")
def test_4():
    print('test_4 executing.....')
@pytest.mark.xfail
@pytest.mark.skipif(False)
def test_5():
    print('test_5 executing.....')
@pytest.mark.xfail
def test_6():
    raise Exception

# collected 6 items
#
# test_marks.py::test_1 test_1 executing.....
# PASSED
# test_marks.py::test_2 test_2 executing.....
# PASSED
# test_marks.py::test_3 test_3 executing.....
# PASSED
# test_marks.py::test_4 SKIPPED (skip because it does not required)
# test_marks.py::test_5 ERROR
# test_marks.py::test_6 XFAIL
# ======= 3 passed, 1 skipped, 1 xfailed, 4 warnings, 1 error in 0.15s ===========
#-----------------------------------------------------------------------------------


