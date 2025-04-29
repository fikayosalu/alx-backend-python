#!/usr/bin/env python3
"""2-measure_runtime module contains a function that uses
the result of an async function"""
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the result of the time taken to execute an
    asyn function"""
    result: list = asyncio.run(wait_n(n, max_delay))
    total_time: float = 0
    for num in result:
        total_time: float = total_time + num
    return total_time/n
