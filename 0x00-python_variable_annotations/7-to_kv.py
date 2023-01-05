#!/usr/bin/env python3
"""Task 7 module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k
    and the square of the int/float v as a float

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The int or float to square.

    Returns:
        Tuple[str, float]: A tuple with the string k and
        the square of v as a float
    """
    return (k, float(v**2))
