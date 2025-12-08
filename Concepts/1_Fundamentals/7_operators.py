"""
Python Operators

Python operators are special symbols used to perform specific operations on one or more operands.
For example, Python's addition operator (+) is used to perform addition operations on two variables, values, or expressions.
"""

# ================================================================================================
# ARITHMETIC OPERATORS
# ================================================================================================

print("=" * 80)
print("🔢 ARITHMETIC OPERATORS")
print("=" * 80)

a = 21
b = 10
c = 0

print(f"\na = {a}, b = {b}")

c = a + b
print(f"✓ Addition (+):        {a} + {b} = {c}")

c = a - b
print(f"✓ Subtraction (-):     {a} - {b} = {c}")

c = a * b
print(f"✓ Multiplication (*):  {a} * {b} = {c}")

c = a / b
print(f"✓ Division (/):        {a} / {b} = {c}")

c = a % b
print(f"✓ Modulus (%):         {a} % {b} = {c}")

a = 2
b = 3
c = a ** b
print(f"✓ Exponent (**):       {a} ** {b} = {c}")

a = 10
b = 5
c = a // b
print(f"✓ Floor Division (//): {a} // {b} = {c}")


# ================================================================================================
# COMPARISON OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("🔍 COMPARISON OPERATORS")
print("=" * 80)

a = 21
b = 10
print(f"\na = {a}, b = {b}")

if a == b:
    print("✓ Equal (==):        a is equal to b")
else:
    print("✓ Equal (==):        a is not equal to b")

if a != b:
    print("✓ Not Equal (!=):    a is not equal to b")
else:
    print("✓ Not Equal (!=):    a is equal to b")

if a < b:
    print("✓ Less Than (<):     a is less than b")
else:
    print("✓ Less Than (<):     a is not less than b")

if a > b:
    print("✓ Greater Than (>):  a is greater than b")
else:
    print("✓ Greater Than (>):  a is not greater than b")

a, b = b, a  # Swap values
print(f"\nAfter swap: a = {a}, b = {b}")

if a <= b:
    print("✓ Less or Equal (<=): a is less than or equal to b")
else:
    print("✓ Less or Equal (<=): a is not less than or equal to b")

if b >= a:
    print("✓ Greater or Equal (>=): b is greater than or equal to a")
else:
    print("✓ Greater or Equal (>=): b is not greater than or equal to a")


# ================================================================================================
# ASSIGNMENT OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("📝 ASSIGNMENT OPERATORS")
print("=" * 80)

a = 21
b = 10
c = 0

print(f"\nInitial: a = {a}, b = {b}, c = {c}")

c = a + b
print(f"✓ c = a + b:        c = {c}")

c += a
print(f"✓ c += a:           c = {c}")

c *= a
print(f"✓ c *= a:           c = {c}")

c /= a
print(f"✓ c /= a:           c = {c}")

c = 2
print(f"✓ Reset c = 2:      c = {c}")

c %= a
print(f"✓ c %= a:           c = {c}")

c **= a
print(f"✓ c **= a:          c = {c}")

c //= a
print(f"✓ c //= a:          c = {c}")


# ================================================================================================
# BITWISE OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("⚙️  BITWISE OPERATORS")
print("=" * 80)

a = 20
b = 10

print(f"\na = {a} ({bin(a)}), b = {b} ({bin(b)})")

c = a & b
print(f"✓ AND (&):           {a} & {b} = {c} ({bin(c)})")

c = a | b
print(f"✓ OR (|):            {a} | {b} = {c} ({bin(c)})")

c = a ^ b
print(f"✓ XOR (^):           {a} ^ {b} = {c} ({bin(c)})")

c = ~a
print(f"✓ Complement (~):    ~{a} = {c} ({bin(c)})")

c = a << 2
print(f"✓ Left Shift (<<):   {a} << 2 = {c} ({bin(c)})")

c = a >> 2
print(f"✓ Right Shift (>>):  {a} >> 2 = {c} ({bin(c)})")


# ================================================================================================
# LOGICAL OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("🔗 LOGICAL OPERATORS")
print("=" * 80)

var = 5
print(f"\nvar = {var}")

print(f"✓ AND (and):  {var} > 3 and {var} < 10 = {var > 3 and var < 10}")
print(f"✓ OR (or):    {var} > 3 or {var} < 4 = {var > 3 or var < 4}")
print(f"✓ NOT (not):  not ({var} > 3 and {var} < 10) = {not (var > 3 and var < 10)}")


# ================================================================================================
# MEMBERSHIP OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("📋 MEMBERSHIP OPERATORS")
print("=" * 80)

a = 10
b = 20
list_data = [1, 2, 3, 4, 5]

print(f"\na = {a}, b = {b}, list = {list_data}")

if a in list_data:
    print(f"✓ in:     {a} is present in the list")
else:
    print(f"✓ in:     {a} is not present in the list")

if b not in list_data:
    print(f"✓ not in: {b} is not present in the list")
else:
    print(f"✓ not in: {b} is present in the list")

c = b / a
print(f"\nc = {b} / {a} = {c}")

if c in list_data:
    print(f"✓ in:     {c} is available in the list")
else:
    print(f"✓ in:     {c} is not available in the list")


# ================================================================================================
# IDENTITY OPERATORS
# ================================================================================================

print("\n" + "=" * 80)
print("🆔 IDENTITY OPERATORS")
print("=" * 80)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(f"\na = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"\n✓ is:     a is c = {a is c}")
print(f"✓ is:     a is b = {a is b}")

print(f"\n✓ is not: a is not c = {a is not c}")
print(f"✓ is not: a is not b = {a is not b}")


# ================================================================================================
# WALRUS OPERATOR (:=)
# ================================================================================================

print("\n" + "=" * 80)
print("🔗 WALRUS OPERATOR (:=)")
print("=" * 80)

print("\n1. Traditional way:")
stack = [1, 2, 3, 4, 5]
n = len(stack)
while len(stack) > 0:
    print(stack.pop(), end=" ")

print("\n\n2. Using walrus operator:")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")

print("\n")