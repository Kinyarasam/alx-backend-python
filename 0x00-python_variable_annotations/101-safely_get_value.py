#!/usr/bin/env python3
"""Task 101 module"""
from typing import Mapping, Union, Any


def safely_get_value(dct: Mapping, key: Any,default: Union[Any, None] = None) -> Union[Any, None]:
    """Return the value for key in dct if it exists, else return default.

    Args:
        dct (Mapping): The dictionary to get the value from.
        key (Any): The key to get the value for.
        default (Union[Any, None]): The default value to return if key is not in dct.

    Returns:
        Union[Any, None]: The value for key in dct, or default if key is not in dct.
    """
    if key in dct:
        return dct[key]
    else:
        return default
