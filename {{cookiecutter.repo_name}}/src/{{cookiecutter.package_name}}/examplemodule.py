"""
This example module shows some simple methods and best practices for documentation
"""

import numpy as np


def hello_world() -> str:
    """
    Method description - A simple method to get the hello world string

    Returns:
       The string "Hello World"
    """
    return "Hello World"


def add_value_to_numpy(array: np.ndarray, amount: float = 1) -> np.ndarray:
    """
    A sample method to add a value to every element in a pandas DataFrame.

    Args:
        array: The source DataFrame to work on.
        amount: The amount to add to each element in the DataFrame

    Returns:
        A new DataFrame with each value increased by amount.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.
        >>> array = np.array([1, 1, 1 ,1, 1])
        >>> result_array = add_value_to_numpy(array, 1)

    """
    if array is None or \
            not isinstance(array, np.ndarray):
        raise ValueError("array must be a valid ndarray")
    # if isinstance(a, np.ndarray):

    return array + amount
