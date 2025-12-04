def largestElementArray(arr):
    max = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1,2,3,4,5,6,7,8,9,10]

output = largestElementArray(arr)

print(output)