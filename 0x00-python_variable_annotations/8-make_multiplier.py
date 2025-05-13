#!/usr/bin/env python3
"""8-make_multiplier contains a function statically typed"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a given
    float by the specified multiplier."""
    def multiply(n: float) -> float:
        """Returns a float multiplied by the multipler"""
        return n * multiplier
    return multiply
