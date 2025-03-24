#!/usr/bin/env python3

"""
Description: Largest Palindrome Product (https://projecteuler.net/problem=4)

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Solution: 906609
"""


def isPalindrome(x):
    return x == x[::-1]


def getLargestPalindromeProduct(n):
    if n <= 0:
        return 0
    if n == 1:
        return 9
    a = 10 ** (n - 1)
    b = 10 ** n - 1
    c = b
    curr = 0
    while c >= a:
        r = 1 if not c % 11 else 11
        d = b if r == 1 or not len(str(c)) % 2 else b - 9
        while d >= c:
            p = c * d
            if p <= curr:
                break
            if isPalindrome(str(p)):
                curr = p
            d -= r
        c -= 1
    return curr


if __name__ == "__main__":
    sol = getLargestPalindromeProduct(3)
    print(sol)
