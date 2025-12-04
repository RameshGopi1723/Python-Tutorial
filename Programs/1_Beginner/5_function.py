def is_prime(num):
    if num <= 1:
        return "Not a Prime Number"
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Not a Prime Number"
        return "Prime Number"


user_input = int(input("Enter the number to check whether the number is prime or not: "))
output = is_prime(user_input)

print("output: ", output)