#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The float to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies \
its float argument by multiplier.
    """
    def multiply(n: float) -> float:
        """Multiply n by multiplier.

        Args:
            n (float): The float to multiply.

        Returns:
            float: The product of n and multiplier.
        """
        return n * multiplier
    return multiply
