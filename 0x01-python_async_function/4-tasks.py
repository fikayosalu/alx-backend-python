#!/usr/bin/env python3
"""4-tasks module contains async/await function"""
import asyncio
from typing import List
from types import CoroutineType

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats in the order of how the
    coroutine was completed"""
    arr: List[asyncio.Future] = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = []
    for item in asyncio.as_completed(arr):
        res: float = await item
        results.append(res)
    return results
