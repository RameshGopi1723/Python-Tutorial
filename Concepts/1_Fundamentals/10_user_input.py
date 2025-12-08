"""
User Input in Python

The input() function allows us to take user input from the keyboard.
By default, input() returns a string. Use type conversion functions like int(), float(), etc.
to convert input to other data types.
"""

# ================================================================================================
# STRING INPUT
# ================================================================================================

print("=" * 80)
print("📝 STRING INPUT")
print("=" * 80)

name = input("\nEnter your name : ")
city = input("Enter your city : ")

print(f"\nHello My name is {name}")
print(f"I am from {city}")


# ================================================================================================
# INTEGER INPUT
# ================================================================================================

print("\n" + "=" * 80)
print("🔢 INTEGER INPUT")
print("=" * 80)

width = int(input("\nEnter width : "))
height = int(input("Enter height : "))

area = width * height
print(f"\nArea of rectangle = {area}")

print("\n" + "=" * 80)