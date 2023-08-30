#!/usr/bin/env python3
""" functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def fn(n: float):
        return n * multiplier
    return fn
