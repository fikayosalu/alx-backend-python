#!/usr/bin/env python3
"""3-task module contains a function for crating an async task"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio Task that wraps wait_random(max_delay)"""
    return asyncio.create_task(wait_random(max_delay))
