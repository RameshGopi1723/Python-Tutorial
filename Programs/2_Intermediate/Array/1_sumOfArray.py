def sumOfArray(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum


arr = [1,2,3,4,5]

output = sumOfArray(arr = arr)
print(output)




#----------------------------------------------

def sumOfArray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


arr = [1,2,3,4,5]

output = sumOfArray(arr = arr)
print(output)