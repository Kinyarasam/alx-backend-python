#!/usr/bin/env python3
"""Task 5 module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum the floats in a list

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in input_list.
    """
    return sum(input_list)
