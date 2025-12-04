#normal approach
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


num = 6

output = factorial(num = num)
print(output)


#Recursive approach
def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n-1)

num = 6

print(fact(n = num))
