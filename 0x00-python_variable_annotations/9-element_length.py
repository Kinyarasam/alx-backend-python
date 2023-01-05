#!/usr/bin/env python3
"""Task 9 module"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element of a lst and its length.

    Args:
        lst (Iterable[Sequence]): The iterable of elements to get the lengths of.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
