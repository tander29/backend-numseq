"""
This module has a single function called fib that is short for fibonacci
what do docstrings normally say?!

author Travis Anderson, tander29
"""


def fib(n):
    """Returns the nth number in the fib sequence!"""
    if n < 2:
        return n
    n += 1
    a, b = 0, 1
    while n > 2:
        result = a + b
        a, b = b, result
        n -= 1
    return result
