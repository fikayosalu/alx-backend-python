#!/usr/bin/env python3
"""2-measure_runtime module contains a coroutine that measures
the runtime of several coroutines"""
import asyncio
import time
from typing import List, Awaitable

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Returns the runtime of the program"""
    start_time: float = time.time()
    task: List[Awaitable] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    return time.time() - start_time
