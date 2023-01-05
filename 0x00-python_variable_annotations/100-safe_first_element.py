#!/usr/bin/env python3
from typing import Any

def safe_first_element(lst: list[Any]) -> Any:
    """Return the first element of lst if it is not empty, else return None.

    Args:
        lst (list[Any]): The list to get the first element of.

    Returns:
        Any: The first element of lst, or None if lst is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

