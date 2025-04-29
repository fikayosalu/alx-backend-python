#!/usr/bin/env python3
""" 1-concurrent_coroutines.py module contains async function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Returns a list of awaitables in order of completion"""
    arr: list[float] = [wait_random(max_delay) for _ in range(n)]
    results: list = []
    for item in asyncio.as_completed(arr):
        res: float = await item
        results.append(res)
    return results
