#!/usr/bin/env python3

"""
Description: Special Pythagorean Triplet (https://projecteuler.net/problem=9)

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

Solution: 31875000
"""


from math import sqrt

def calcGCD(a, b):
    while b:
        a, b = b, a % b
    return a

def getTriplets(s):
    s //= 2
    limit = int(sqrt(s))
    triplets = []
    m = 2
    while m <= limit:
        if not s % m:
            s_m = s // m
            while not s_m % 2:
                s_m //= 2
            k = m + 2 if m % 2 else m + 1
            while k <= s_m and k < (2 * m):
                if not s_m % k and calcGCD(m, k) == 1:
                    n = k - m
                    d = s // (k * m)
                    a = (m ** 2 - n ** 2) * d
                    b = 2 * m * n * d
                    c = (m ** 2 + n ** 2) * d
                    triplets.append((a,b,c))
                k += 2
        m += 1
    return triplets


def getTripletProduct(tripletSum):
    triplets = getTriplets(tripletSum)
    products = []
    for a, b, c in triplets:
        products.append(a * b * c)
    return products


if __name__ == "__main__":
    sol = getTripletProduct(1000)
    print(sol)
