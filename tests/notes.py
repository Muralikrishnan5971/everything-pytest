"""
********* PYTEST **********

To run pytest, we have options to specify files and directories. if don't specify any files or directories, 
pytest will look for tests in the current working directory and its subdirectories. 
It looks for .py files starting with test_ or ending with _test.

pytest --tb=no
--tb=no flag turns off traceback, can we used when we don't want to see full output.
--tb=short   ---> shorted traceback format

pytest --tb=no test_one.py test_two.py   -- the same can be acheived by only mentioning the directory

pytest --tb=no tests

pytest --tb=no tests/test_one.py::test_passing

TEST DISCOVERY
--------------

The part of test execution where pytest goes off and finds which tests to run is called test discovery.
Given no arguments, pytest looks at your current directory and all subdirectories for test files and runs the
test code it finds. If we give pytest a filename, directory name or a list of those, it looks there instead
of the current directory.

Naming convention to keep your test code disciverable by pytest:

test files -----> test_<filename>.py or <filename>_test.py
test functions ---> test_<functionname>
test class ---> Test<classname>

Again the above test discovery rules can be altered using configurations files

ALL POSSIBLE OUTCOMES OF A TEST:

-> PASSED(.)  -- The test ran successfully.
-> FAILED(F)  -- The test did not run successfully.
-> SKIPPED(s) -- the test was skipped. we can tell pytest to skip a test by using either
@pytest.mark.skip() or @pytest.mark.skipif() decorators.
-> XFAIL(x)   -- The test is not supposed to pass, and it ran and failed. we can tell 
pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator.
-> XPASS(X)   -- This test was marked with xfail, but it ran and passed.
-> ERROR(E)   -- An exception happened either during the execution of a fixture or hook function,
And not during the execution of a test function.


pytest -vv test_fail.py   ---> show more information on the failure

Failing a test using pytest.fail()

A test fails if there is any uncaught exception. This can happen if

-> an assert statement fails, which will raise an AssertionError exception,
-> the test code calls pytest.fail() which will raise an exception, or
-> any other exception is raised

Only in rare case where assert is not suitable, use pytest.fail().

When calling pytest.fail() or raising an exception directly, we don't get the wonderful assert
rewriting provided by pytest. However, there are resonable times to use pytest.fail(),
such as in an assertion helper.

An Assertion helper is an function that is used to wrap up a complicated assertion check.

Note that assert rewriting is only applied to conftest.py files and test files.
see pytest documentation for more details.

Testing for Expected Exceptions using pytest.raises()
























"""