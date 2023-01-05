#!/usr/bin/env python3
"""Task 101 module"""
from typing import Dict, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """Return the value for key in dct if it exists, else return default.

    Args:
        dct (Dict[str, T]): The dictionary to get the value from.
        key (str): The key to get the value for.
        default (T): The default value to return if key is not in dct.

    Returns:
        T: The value for key in dct, or default if key is not in dct.
    """
    if key in dct:
        return dct[key]
    else:
        return default
