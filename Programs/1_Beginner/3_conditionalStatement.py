#Odd or Even function
def oddEven(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
    
    
user_input = int(input("Enter the number to check Odd or Even: "))

print(oddEven(num = user_input))