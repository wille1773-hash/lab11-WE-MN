#https://github.com/wille1773-hash/lab11-WE-MN.git
#Partner1: William Evans
#Partner2: Matthew Nunes
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def log(a, b):
    if a <= 0 or a == 1  or b <= 0:
        raise ValueError("invalid base or argument for logarithm")
    return math.log(b, a)
def exp(a, b):
    return a ** b
