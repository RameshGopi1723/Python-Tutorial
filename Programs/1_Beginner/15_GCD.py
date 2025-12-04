# loop until the remainder is 0
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

a = 60  # first number
b = 48  # second number

ouput = gcd(a,b)
print(ouput) 
