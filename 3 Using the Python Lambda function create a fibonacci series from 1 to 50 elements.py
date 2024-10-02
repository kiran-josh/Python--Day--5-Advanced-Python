"""
Name: Kiran G
Program: Using the Python Lambda function create a fibonacci series from 1 to 50 elements?

"""

from functools import reduce

# Function to generate Fibonacci series using reduce
def fibonacci(n):
    fib_series = [0, 1]  # Starting elements of Fibonacci series
    reduce(lambda x, _: fib_series.append(x[-1] + x[-2]), range(n - 2), fib_series)
    return fib_series[:n]

# Generate Fibonacci series for the first 50 elements
fib_50 = fibonacci(50)

# Print the Fibonacci series
print(fib_50)
