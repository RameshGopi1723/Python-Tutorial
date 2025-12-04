#using normal function
def addFunction(a, b):
    return a + b

addition = addFunction(a = 17, b = 23)
print(addition)



#using lambda function
add = lambda a, b : a + b

print(add(a = 17, b = 23))