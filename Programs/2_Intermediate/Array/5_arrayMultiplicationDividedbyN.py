def arrayMultiplicationDivideN(array, num):
    mul = 1
    for i in range(0, len(array)):
        mul *= array[i]
    return mul % num


array = [100, 10, 5, 25, 35, 14]
num = 11

output = arrayMultiplicationDivideN(array, num)

print(output)