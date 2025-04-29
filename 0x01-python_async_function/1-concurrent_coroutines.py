#!/usr/bin/env python3
"""1-concurrent_coroutines module contains async/await function"""
import asyncio
from typing import List
from types import CoroutineType

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats in the order of how the
    coroutine was completed"""
    arr: List[asyncio.Future] = [wait_random(max_delay) for _ in range(n)]
    results: List[float] = []
    for item in asyncio.as_completed(arr):
        res: float = await item
        results.append(res)
    return results
