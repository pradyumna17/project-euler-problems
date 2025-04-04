#!/usr/bin/env python3

"""
Description: Smallest Multiple (https://projecteuler.net/problem=5)

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

Solution: 232792560
"""


from math import sqrt


def sieveOfEratosthenes(n):
    sieve = [True] * n
    limit = int(sqrt(n))
    i = 2
    while i <= limit:
        if sieve[i]:
            for mult in range(i ** 2, n, i):
                sieve[mult] = False
        i += 1
    return [prime for prime in range(2, n) if sieve[prime]]


def getPrimeFactorsFreq(n):
    if n <= 2:
        return {n: 1}
    factors = []
    limit = int(sqrt(n)) + 1
    primes = sieveOfEratosthenes(limit)
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)
    return countFreq(factors)


def countFreq(lst):
    freq = {}
    for each in lst:
        if each not in freq:
            freq[each] = 0
        freq[each] += 1
    return freq


def getSmallestDivisibleNumber(high, low=1):
    if high <= 0 or low <= 0:
        return 0
    globalFreq = getPrimeFactorsFreq(low)
    for i in range(low + 1, high + 1):
        localFreq = getPrimeFactorsFreq(i)
        for num in localFreq:
            if num not in globalFreq or localFreq[num] > globalFreq[num]:
                globalFreq[num] = localFreq[num]
    s = 1
    for num, val in globalFreq.items():
        s *= num ** val
    return s


if __name__ == "__main__":
    sol = getSmallestDivisibleNumber(20)
    print(sol)
