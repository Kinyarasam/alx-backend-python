#!/usr/bin/env python3
"""Task 100 module"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if it is not empty, else return None.

    Args:
        lst (Sequence[Any]): The sequence to get the first element of.

    Returns:
        Union[Any, None]: The first element of lst, or None if lst is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
