import math

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(n):
    # A number is Fibonacci if and only if one of (5*n*n + 4) or (5*n*n - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Example usage
num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is NOT a Fibonacci number.")
