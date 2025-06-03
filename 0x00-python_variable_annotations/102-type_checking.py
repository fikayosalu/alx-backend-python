#!/usr/bin/env python3
""" 102-type_checking """

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a new list where each element in the tuple
    is repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Must be a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Pass an int, not float
