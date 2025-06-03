#!/usr/bin/env python3
""" 100-safe_first_element """

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element or None if the sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
