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
    a = 10 ** (n - 1)
    b = 10 ** n - 1
    c = b
    curr = 0
    while c >= a:
        d = b
        while d >= c:
            p = c * d
            if p <= curr:
                break
            if isPalindrome(str(p)):
                curr = p
            d -= 1
        c -= 1
    return curr


if __name__ == "__main__":
    sol = getLargestPalindromeProduct(3)
    print(sol)
