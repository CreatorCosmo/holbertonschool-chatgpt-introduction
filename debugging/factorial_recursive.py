#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursive method.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the number 'n'.
    """
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n-1)

# Read an integer from command line argument, compute its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
