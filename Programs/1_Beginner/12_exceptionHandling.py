def exceptionHandling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero..!"


a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

output = exceptionHandling(a = a, b = b)
print(output)