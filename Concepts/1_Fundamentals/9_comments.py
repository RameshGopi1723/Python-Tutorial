"""
Comments in Python

Python comments are programmer-readable explanation or annotations in the Python source code. 
They are added with the purpose of making the source code easier for humans to understand, 
and are ignored by Python interpreter. Comments enhance the readability of the code and help 
the programmers to understand the code very carefully.
"""

# ================================================================================================
# SINGLE-LINE COMMENTS
# ================================================================================================

print("=" * 80)
print("💬 SINGLE-LINE COMMENTS")
print("=" * 80)

# Standalone single line comment is placed here
def greet():
    print("Hello, World!")

print("\n1. Standalone Comment:")
greet()

# Inline single line comment is placed here
print("\n2. Inline Comment:")
print("Hello, World!")  # Inline single line comment is placed here


# ================================================================================================
# MULTI-LINE COMMENTS
# ================================================================================================

print("\n" + "=" * 80)
print("📝 MULTI-LINE COMMENTS")
print("=" * 80)

# This function calculates the factorial of a number
# using an iterative approach. The factorial of a number
# n is the product of all positive integers less than or
# equal to n. For example, factorial(5) is 5*4*3*2*1 = 120.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("\n1. Using Multiple Single-Line Comments:")
number = 5
print(f"   The factorial of {number} is {factorial(number)}")


# ================================================================================================
# DOCSTRINGS
# ================================================================================================

print("\n" + "=" * 80)
print("📚 DOCSTRINGS")
print("=" * 80)

"""
This function calculates the greatest common divisor (GCD)
of two numbers using the Euclidean algorithm. The GCD of
two numbers is the largest number that divides both of them
without leaving a remainder.
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("\n1. Multi-line Docstring (GCD Function):")
result = gcd(48, 18)
print(f"   The GCD of 48 and 18 is: {result}")


def greet(name):
    """
    This function greets the person whose name is passed as a parameter.

    Parameters:
    name (str): The name of the person to greet

    Returns:
    None
    """
    print(f"   Hello, {name}!")

print("\n2. Function Docstring (greet Function):")
greet("Alice")

print("\n" + "=" * 80)