#!/usr/bin/env python3

"""
Description: Summation of Primes (https://projecteuler.net/problem=10)

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
Find the sum of all the primes below two million.

Solution: 142913828922
"""


from math import sqrt


def getPrimeSum(n):
    if n < 2:
        return 0
    sieve = [True] * (n // 2)
    i = 1
    limit = (int(sqrt(n)) - 1) // 2
    while i <= limit:
        if sieve[i]:
            for mult in range(2 * i * (i + 1), n // 2, 2 * i + 1):
                sieve[mult] = False
        i += 1
    s = 2
    for i in range(1, n // 2):
        if sieve[i]:
            s += (2 * i + 1)
    return s


if __name__ == "__main__":
    sol = getPrimeSum(2000000)
    print(sol)
