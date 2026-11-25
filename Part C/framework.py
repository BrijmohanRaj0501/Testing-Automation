# which framework you used in your automation framework?
#--> PYTest and POM framework, I have used in my framework
from unittest import skip


# Framework :- A framework is a set of guidelines ad standards used to organize
#              the automation scripts.

# Benefits :-
#1. reusability
#2. Maintainability
#3. Readability
#4. tests data management
#5. Reporting
#6. Team collaboration
#7. Scalability


# pytest--> Pytest is a python testing framework used to write, organize, execute,
#           manage tests cases.

#      pip install pytest    # installation

# Features :-
# #simple and easy to write testcase
# markers - select and use only selected testcase
# fixtures - making tests case reusable
# powerful assertion - showing testcase pass or failing
# parameterization-
# report generation is possible.


#rules:-
# 1. Filename should start with "test_" or end with "_test".
#   Eg: test_filename or filename_test

# 2. Function name should start with "test_".
#    Eg: def test_functionName():
#         pass

# 3. Classname should start with tests
#  Eg: class TestClassName:
#       Pass



# To move forward in terminal we have cd<space>filename
#
# To move backward we have cd ..
#
#  to execute a particular file in Terminal we have a syntax:
#          py -m pytest -v .\test_file1.py
#                       OR
#          pytest -vs .\test_file1.py
#                       OR
#          py -m pytest -vs .\test_file1.py

# to execute all the tests function in a folder:
#        py -m pytest -vs

# suppose if any testcase failed, it will not geting affect the execution of others.





# markers - select and use only selected testcase
# syntax- @pytest.mark.markername
## write these testcase above all the testcase_function we need to execute

# in terminal we write--> py -m pytest -vs <filename> -m <markername>
# we can mark one test_case for multiple markers.

# types of markers:
# 1. custom markers -> custom markers are used to group related tests case
# syntax= @pytest.mark.<markername>


# 2. skip markers -> to skip the execution of tests cases we use skip markers
#                    this is an unconditional skip
#syntax= @pytest.mark.skip(reason="reason to skip")-> reason is an optional parameter

# 3. skip if markers -> which is used to skip the execution of testcases but skip is based on the condition.
# syntax= @pytest.mark.skipif(condition,reason) -> reason is mandatory parameter
#                                               if we skip reason , we will get error
#                                               if we skip the condition , by default it will considerd as True
#           if the condition is true , it will skip the testcases
#           if the condition is false , it will execute the testcases


# 4. xfail -> xfail stands for expected failure--> this is an expected failure
# this is used when we know the testcase are getting failed

# syntax= @pytest.mark.xfail
# if the testcase fail--> output is xfail
# if the testcase are expected to fail but in some case it will pass the testcase
#                               then the output is xpassed


# parameterized ->
# it is used to run same testcases multiples times with different input data
# syntax =@pytest.mark.parameterize("a,b",[('asd','asdf'),('asd','asdf'),('asd','asdf')])






# fixture -> it is a function block which holds common functionality.
# it is a reusable function used to give skip and Teardown
# syntax = @pytest.fixture

# advantage=
# 1. code reuse
# 2. code duplication is reduced
# 3. better maintenance
# 4, provide setup and Teardown support

# example:

    # open browser,webpage ---------> setup
    # tests login
    # close the browser ---------> Teardown

    # open browser,webpage ---------> setup
    # tests add to cart
    # close the browser ---------> Teardown

    # open browser,webpage ---------> setup
    # tests logout
    # close the browser ---------> Teardown


# setup-> the set of operation before the execution of tests function.
# Teardown -> the set of operation after the execution of tests function.


# autouse=True --> when we use it, by default fixture is going to apply on all function.
# without passing the name of fixture as parameter to tests function

# scope:
    # 1. Class = fixture will apply on whole class at once

    # 2. function = by default it will be scope as function









