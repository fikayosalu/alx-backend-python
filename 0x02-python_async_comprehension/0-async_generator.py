#!/usr/bin/env python3
"""0-async_generator module contains a coroutine
which is an async generator function"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """Async Generator function that returns a random float from 1-10
    every second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
