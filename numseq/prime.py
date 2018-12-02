"""
This module defines prime numbers and returns a list of primes

Author: Travis Anderson, tander29
"""


def is_prime(m):
    """Return bool if number is Prime """
    prime = True
    if m > 2:
        for i in range(2, m):
            if m % i == 0:
                prime = False
            if i * i > m:
                # this is for speeding up calculation time
                break
    return prime


def primes(n):
    """Return list of primes """
    prime_list = []
    for i in range(n):
        if is_prime(i) and i > 1:
            prime_list.append(i)
    return prime_list
