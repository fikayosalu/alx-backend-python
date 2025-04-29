#!/usr/bin/env python3
"""0-basic_async_syntax module uses async/await functions"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """The function waits for a random delay between 0 and max_delay
    and returns the delay value"""
    value: float = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
