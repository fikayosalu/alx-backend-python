#!/usr/bin/env python3
"""Module that demonstrates asynchronous comprehension in Python."""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Returns:list[float]: A list containing 10 float
    numbers generated asynchronously"""
    result: List[float] = [x async for x in async_generator()]
    return result
