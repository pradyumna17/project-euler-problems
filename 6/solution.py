#!/usr/bin/env python3

"""
Description: Sum Square Difference (https://projecteuler.net/problem=6)

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

Solution: 25164150
"""


def getSumSquareDifference(n):
    s1 = n * (n + 1) // 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    return s1 ** 2 - s2


if __name__ == "__main__":
    sol = getSumSquareDifference(100)
    print(sol)
