#!/usr/bin/env python3

"""
Description: https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Solution: 6857
"""

from math import sqrt, ceil


def getLargestPrimeFactor(n):
    if n <= 2:
        return n
    factors = []
    limit = ceil(sqrt(n))
    i = 2
    while n > 1 and i <= limit:
        if not n % i:
            factors.append(i)
            n = n // i
        i += 1
    return max(factors) if factors else n


if __name__ == "__main__":
    sol = getLargestPrimeFactor(600851475143)
    print(sol)
