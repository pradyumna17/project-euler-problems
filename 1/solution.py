#!/usr/bin/env python3

"""
Description: Multiples of 3 or 5 (https://projecteuler.net/problem=1)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Solution: 233168
"""


def sumOfDivisors(n, target):
    x = target // n
    return int(n * x * (x + 1) / 2)


if __name__ == "__main__":
    target = 999
    sol = sumOfDivisors(3, target) + sumOfDivisors(5, target) - sumOfDivisors(15, target)
    print(sol)
