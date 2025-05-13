#!/usr/bin/env python3
" 9-element_length contains a function that is statically typed"
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence,
                                                          int]]:
    """Returns a list of tuples where each tuple contains
    an element from the input iterable and its length."""
    return [(i, len(i)) for i in lst]
