# file 2: test_string.py
def test_verify():
    assert "python".upper() == 'PYTHON'
def test_length():
    assert len("automation") == 10
def test_startwith():
    assert "selenium".startswith('sel')
def test_endwith():
    assert 'pytest'.endswith('ing'),'not ending with ing'
def test_samplelen():
    assert len('sample') == 6

# collected 5 items
#
# test_string.py::test_verify PASSED
# test_string.py::test_length PASSED
# test_string.py::test_startwith PASSED
# test_string.py::test_endwith FAILED
# test_string.py::test_samplelen PASSED


# execute all tests cases
# collected 10 items
#
# test_math.py::test_sum FAILED                                                                                                               [ 10%]
# test_math.py::test_product FAILED                                                                                                           [ 20%]
# test_math.py::test_divisible PASSED                                                                                                         [ 30%]
# test_math.py::test_square PASSED                                                                                                            [ 40%]
# test_math.py::test_verify FAILED                                                                                                            [ 50%]
# test_string.py::test_verify PASSED                                                                                                          [ 60%]
# test_string.py::test_length PASSED                                                                                                          [ 70%]
# test_string.py::test_startwith PASSED                                                                                                       [ 80%]
# test_string.py::test_endwith FAILED                                                                                                         [ 90%]
# test_string.py::test_samplelen PASSED









