#!/usr/bin/env python3
'''implementing type annotations.'''
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list and return a list of tuples
    where each tuple contains the original element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., list, string, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence
            from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
