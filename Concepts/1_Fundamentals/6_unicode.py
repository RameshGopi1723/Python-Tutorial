"""
Unicode in Python

Unicode assigns unique numbers to characters from all languages.
- Code Point: Unique number for each character (e.g., U+0041 for 'A')
- UTF-8: Standard encoding (1-4 bytes per character)
- Python 3 uses Unicode by default
"""

# ================================================================================================
# UNICODE BASICS
# ================================================================================================

print("=" * 80)
print("📚 UNICODE BASICS")
print("=" * 80)

print("\n1. Plain Text vs Unicode:")
var = "3/4"
print(f"   Plain text: {var}")

var = "\u00BE"
print(f"   Unicode (\\u00BE): {var}")

print("\n2. Multiple Unicode Characters:")
var = "\u0031\u0030"
print(f"   Unicode (\\u0031\\u0030): {var}")


# ================================================================================================
# ENCODING & DECODING
# ================================================================================================

print("\n" + "=" * 80)
print("🔄 ENCODING & DECODING")
print("=" * 80)

print("\n1. String to Bytes (encode):")
string = "Hello"
tobytes = string.encode('utf-8')
print(f"   String: '{string}'")
print(f"   Bytes: {tobytes}")

print("\n2. Bytes to String (decode):")
string = tobytes.decode('utf-8')
print(f"   Bytes: {tobytes}")
print(f"   String: '{string}'")

print("\n3. Currency Symbol Encoding (₹):")
string = "\u20B9"
print(f"   Character: {string}")
tobytes = string.encode('utf-8')
print(f"   Encoded: {tobytes}")
string = tobytes.decode('utf-8')
print(f"   Decoded: {string}")