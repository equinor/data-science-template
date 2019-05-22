import os
import sys

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

# from pandas.util.testing import assert_frame_equal
from examplepackage import examplemodule


def test_something():
    # print(os.getcwd())
    assert True, "A comment to show if the test fails"


# def test_that_fails():
#     assert False, "We expected this to fail"


def test_hello_world():
    assert examplemodule.hello_world() == "Hello World", "The Hello World strings should be the same"
