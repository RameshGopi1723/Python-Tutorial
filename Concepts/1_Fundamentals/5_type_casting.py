# Type Casting in Python

"""
Python Type Casting is a process in which we convert a literal of one data type 
to another data type. Python supports two types of casting:
  1. Implicit Casting - automatic conversion by Python
  2. Explicit Casting - manual conversion by programmer
"""

# ================================================================================================
# IMPLICIT TYPE CASTING
# ================================================================================================
# Python automatically converts one data type to another in certain operations.

print("=" * 80)
print("🔄 IMPLICIT TYPE CASTING")
print("=" * 80)

# Int + Float = Float
print("\n1. Integer + Float:")
a = 10
b = 10.5
c = a + b
print(f"   {a} (int) + {b} (float) = {c} ({type(c).__name__})")

# Bool + Float = Float
print("\n2. Boolean + Float:")
a = True
b = 10.5
c = a + b
print(f"   {a} (bool) + {b} (float) = {c} ({type(c).__name__})")

# Bool + Int = Int
print("\n3. Boolean + Integer:")
a = False
b = 5
c = a + b
print(f"   {a} (bool) + {b} (int) = {c} ({type(c).__name__})")


# ================================================================================================
# EXPLICIT TYPE CASTING - INT()
# ================================================================================================
# Convert other data types to integer.

print("\n" + "=" * 80)
print("🔢 EXPLICIT TYPE CASTING - INT()")
print("=" * 80)

# Float to Int (truncates decimal)
print("\n1. Float to Integer:")
a = int(10.5)
print(f"   int(10.5) = {a}")

# Float expression to Int
print("\n2. Float Expression to Integer:")
a = int(2 * 3.14)
print(f"   int(2 * 3.14) = {a}")

# String to Int
print("\n3. String to Integer:")
a = int("100")
print(f"   int('100') = {a} ({type(a).__name__})")

# String concatenation to Int
print("\n4. String Concatenation to Integer:")
result = "10" + "01"
print(f"   '10' + '01' = {result} ({type(result).__name__})")
result_int = int("10" + "01")
print(f"   int('10' + '01') = {result_int} ({type(result_int).__name__})")

# Bool to Int
print("\n5. Boolean to Integer:")
a = int(True)
b = int(False)
print(f"   int(True) = {a}")
print(f"   int(False) = {b}")


# ================================================================================================
# EXPLICIT TYPE CASTING - FLOAT()
# ================================================================================================
# Convert other data types to float.

print("\n" + "=" * 80)
print("🔢 EXPLICIT TYPE CASTING - FLOAT()")
print("=" * 80)

# Int to Float
print("\n1. Integer to Float:")
a = float(10)
print(f"   float(10) = {a}")

# String to Float
print("\n2. String to Float:")
a = float("10.5")
print(f"   float('10.5') = {a}")

# Bool to Float
print("\n3. Boolean to Float:")
a = float(True)
b = float(False)
print(f"   float(True) = {a}")
print(f"   float(False) = {b}")


# ================================================================================================
# EXPLICIT TYPE CASTING - STR()
# ================================================================================================
# Convert other data types to string.

print("\n" + "=" * 80)
print("📝 EXPLICIT TYPE CASTING - STR()")
print("=" * 80)

# Int to String
print("\n1. Integer to String:")
a = str(100)
print(f"   str(100) = '{a}' ({type(a).__name__})")

# Float to String
print("\n2. Float to String:")
a = str(10.5)
print(f"   str(10.5) = '{a}' ({type(a).__name__})")

# Bool to String
print("\n3. Boolean to String:")
a = str(True)
b = str(False)
print(f"   str(True) = '{a}'")
print(f"   str(False) = '{b}'")

# List to String
print("\n4. List to String:")
a = str([1, 2, 3])
print(f"   str([1, 2, 3]) = '{a}' ({type(a).__name__})")


# ================================================================================================
# EXPLICIT TYPE CASTING - BOOL()
# ================================================================================================
# Convert other data types to boolean.

print("\n" + "=" * 80)
print("✅ EXPLICIT TYPE CASTING - BOOL()")
print("=" * 80)

# Int to Bool (0=False, non-zero=True)
print("\n1. Integer to Boolean:")
print(f"   bool(0) = {bool(0)}")
print(f"   bool(1) = {bool(1)}")
print(f"   bool(5) = {bool(5)}")
print(f"   bool(-1) = {bool(-1)}")

# String to Bool (empty=False, non-empty=True)
print("\n2. String to Boolean:")
print(f"   bool('') = {bool('')}")
print(f"   bool('Hello') = {bool('Hello')}")

# Float to Bool (0.0=False, non-zero=True)
print("\n3. Float to Boolean:")
print(f"   bool(0.0) = {bool(0.0)}")
print(f"   bool(1.5) = {bool(1.5)}")

# List to Bool (empty=False, non-empty=True)
print("\n4. List to Boolean:")
print(f"   bool([]) = {bool([])}")
print(f"   bool([1, 2, 3]) = {bool([1, 2, 3])}")


# ================================================================================================
# EDGE CASES & ERROR HANDLING
# ================================================================================================

print("\n" + "=" * 80)
print("⚠️  EDGE CASES & ERROR HANDLING")
print("=" * 80)

# Invalid string to int
print("\n1. Invalid String to Integer (ValueError):")
try:
    a = int("abc")
except ValueError as e:
    print(f"   ✗ int('abc') → ValueError: {e}")

# Invalid string to float
print("\n2. Invalid String to Float (ValueError):")
try:
    a = float("12.5.6")
except ValueError as e:
    print(f"   ✗ float('12.5.6') → ValueError: {e}")

# None to int
print("\n3. None to Integer (TypeError):")
try:
    a = int(None)
except TypeError as e:
    print(f"   ✗ int(None) → TypeError: {e}")

# Valid edge cases
print("\n4. Valid Edge Cases:")
print(f"   int('0') = {int('0')}")
print(f"   int('-5') = {int('-5')}")
print(f"   float('inf') = {float('inf')}")
print(f"   float('-inf') = {float('-inf')}")


# ================================================================================================
# TYPE CHECKING
# ================================================================================================

print("\n" + "=" * 80)
print("🔍 TYPE CHECKING")
print("=" * 80)

a = 10
b = 10.5
c = "Hello"
d = True

print(f"\ntype({a}) = {type(a)}")
print(f"type({b}) = {type(b)}")
print(f"type('{c}') = {type(c)}")
print(f"type({d}) = {type(d)}")

print(f"\nisinstance({a}, int) = {isinstance(a, int)}")
print(f"isinstance({b}, float) = {isinstance(b, float)}")
print(f"isinstance('{c}', str) = {isinstance(c, str)}")
print(f"isinstance({d}, bool) = {isinstance(d, bool)}")