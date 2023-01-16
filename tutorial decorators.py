import random
from typing import List, Any, Iterable
from types import FunctionType
from functools import wraps, reduce
from sys import stderr


class Multiplier:
    def __init__(self, k: Any):
        self.k = k
        
    def __call__(self, v: float):
        return v * self.k

a = 9
l = (2, 3, "abc")
doubler = Multiplier(2)
print(list(map(doubler, range(a))))

tripler = Multiplier(3)