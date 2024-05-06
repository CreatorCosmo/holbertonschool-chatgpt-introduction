#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        input_number = int(sys.argv[1])
        f = factorial(input_number)
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
else:
    print("Error: No input provided. Please provide an integer for factorial calculation.")
