#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. It is denoted by n! and defined as:
    n! = n × (n-1) × (n-2) × ... × 3 × 2 × 1
    By definition, 0! = 1.
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
             Must be >= 0.
    
    Returns:
    int: The factorial of the given integer n.
    
    Raises:
    RecursionError: If n is too large and exceeds maximum recursion depth.
    ValueError: If n is negative (though not explicitly handled in this function).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the factorial argument from command line and calculate the result
f = factorial(int(sys.argv[1]))
print(f)