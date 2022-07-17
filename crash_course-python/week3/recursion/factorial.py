#!/usr/bin/python3
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)
