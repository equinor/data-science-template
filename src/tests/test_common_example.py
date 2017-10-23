import os
import sys
import numpy as np
import pytest
# from pandas.util.testing import assert_frame_equal
from src.common import example


def test_something():
    # print(os.getcwd())
    assert True, "A comment to show if the test fails"


def test_common_example_hello_world():
    assert example.hello_world() == "Hello World", "The Hello World strings should be the same"


def test_common_example_add_value_to_numpy():
    array = np.array([1, 1, 1, 1, 1])
    expected_result = np.array([2, 2, 2, 2, 2])
    result_array = example.add_value_to_numpy(array, 1)
    assert np.array_equal(expected_result, result_array), "The Hello World strings should be the same"


def test_common_example_add_value_to_numpy_wrong_type():
    with pytest.raises(ValueError) as e_info:
        example.add_value_to_numpy([1,1], 1)


def test_common_example_add_value_to_numpy_empty():
    with pytest.raises(ValueError) as e_info:
        example.add_value_to_numpy(None, 1)


# def test_that_fails():
#     assert False, "We expected this to fail"
