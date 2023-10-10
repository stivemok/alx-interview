#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """calculates the fewest number of operations"""
    if n < 2:
        return 0
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(int(n/i)) + i
