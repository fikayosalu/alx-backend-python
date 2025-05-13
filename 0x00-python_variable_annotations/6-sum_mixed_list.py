#!/usr/bin/env python3
"""6-sum_mixed_list contains a function that is statically typed"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts a list of integers and floats and returns the sum"""
    return sum(mxd_lst)
