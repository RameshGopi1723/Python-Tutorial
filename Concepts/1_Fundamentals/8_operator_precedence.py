"""
Operator Precedence in Python

An expression may have multiple operators to be evaluated. 
The operator precedence defines the order in which operators are evaluated. 
In other words, the order of operator evaluation is determined by the operator precedence.

Precedence Order (High to Low):
  1. Parentheses ()
  2. Exponent **
  3. Multiplication *, Division /, Floor Division //, Modulus %
  4. Addition +, Subtraction -
  5. Comparison ==, !=, <, >, <=, >=
  6. Logical NOT, AND, OR
"""

# ================================================================================================
# OPERATOR PRECEDENCE EXAMPLES
# ================================================================================================

print("=" * 80)
print("📊 OPERATOR PRECEDENCE EXAMPLES")
print("=" * 80)

a = 20
b = 10
c = 15
d = 5
e = 0

print(f"\na = {a}, b = {b}, c = {c}, d = {d}")

print("\n1. (a + b) * c / d")
print(f"   = ({a} + {b}) * {c} / {d}")
e = (a + b) * c / d
print(f"   = (30 * 15) / 5")
print(f"   = {e}")

print("\n2. ((a + b) * c) / d")
print(f"   = (({a} + {b}) * {c}) / {d}")
e = ((a + b) * c) / d
print(f"   = ((30) * 15) / 5")
print(f"   = {e}")

print("\n3. (a + b) * (c / d)")
print(f"   = ({a} + {b}) * ({c} / {d})")
e = (a + b) * (c / d)
print(f"   = (30) * (3.0)")
print(f"   = {e}")

print("\n4. a + (b * c) / d")
print(f"   = {a} + ({b} * {c}) / {d}")
e = a + (b * c) / d
print(f"   = 20 + (150 / 5)")
print(f"   = {e}")

print("\n" + "=" * 80)