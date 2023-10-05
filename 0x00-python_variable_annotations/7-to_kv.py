#!/usr/bin/python3
'''implementing type annotations.'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the input string and the square of the integer or
    float.
    Args:
        k (str): The input string.
        v (Union[int, float]): An integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and
        the square of v as a float.
    """
    squared = float(v) ** 2
    return k, squared
