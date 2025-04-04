#!/usr/bin/env python3

"""
Description: 10001st Prime (https://projecteuler.net/problem=7)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
What is the 10001st prime number?

Solution: 104743
"""


from math import log, sqrt


def getNthPrime(n):
    if n < 6:
        primes = [2, 3, 5, 7, 11]
        return primes[n - 1]
    ubound = int(n * log(n) + n * log(log(n))) + 1
    sieve = [True] * (ubound)
    limit = int(sqrt(ubound))
    i = 2
    while i <= limit:
        if sieve[i]:
            for mult in range(i ** 2, ubound, i):
                sieve[mult] = False
        i += 1
    primes = [prime for prime in range(2, ubound) if sieve[prime]]
    return primes[n - 1]


if __name__ == "__main__":
    sol = getNthPrime(10001)
    print(sol)
