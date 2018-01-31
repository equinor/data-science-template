import os
import sys
import numpy as np
import pytest

# Explicitly set path so don't need to run setup.py - if we have multiple copies of the code we would otherwise need
# to setup a separate environment for each to ensure the code pointers are correct.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

# from pandas.util.testing import assert_frame_equal
from examplepackage import examplemodule


def test_add_value_to_numpy():
    array = np.array([1, 1, 1, 1, 1])
    expected_result = np.array([2, 2, 2, 2, 2])
    result_array = examplemodule.add_value_to_numpy(array, 1)
    assert np.array_equal(expected_result, result_array), "The Hello World strings should be the same"


def test_add_value_to_numpy_wrong_type():
    with pytest.raises(ValueError) as e_info:
        examplemodule.add_value_to_numpy([1, 1], 1)


def test_add_value_to_numpy_empty():
    with pytest.raises(ValueError) as e_info:
        examplemodule.add_value_to_numpy(None, 1)
