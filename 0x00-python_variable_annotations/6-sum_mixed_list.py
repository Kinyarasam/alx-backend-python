#!/usr/bin/env python3
"""Task 6 module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum the integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list of integers \
and floats to sum.

    Returns:
        float: The sum of the integers and floats in mxd_lst.
    """
    return sum(mxd_lst)
