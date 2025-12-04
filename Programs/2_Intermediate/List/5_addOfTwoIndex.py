def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if target == arr[j] + arr[i]: 
                return [i, j]
    return []


arr = [1,2,3,4,5]
print(twoSum(arr = arr, target = 9))