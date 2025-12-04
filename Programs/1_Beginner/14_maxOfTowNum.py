def maxOfTwo(a,b):
    if a > b:
        return a
    elif a == b:
        return "Both are same"
    else:
        return b 


res = maxOfTwo(a = 10, b = 10)

print("Greater Number: ",res)



#using ternary operator 
a = 1
b = 2

res = a if a > b else b

print(res)