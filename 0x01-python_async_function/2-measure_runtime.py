#!/usr/bin/env python3
"""Task 2's modules"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Comutes the average runtime of wait_n.

    Args:
        n (int): number
        max_delay (int): maximum delay

    Returns:
        (float):
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
