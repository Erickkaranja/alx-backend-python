#!/usr/bin/python3

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the input_list as a float.
    """
    total = sum(input_list)
    return float(total)
