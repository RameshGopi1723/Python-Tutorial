def linearSearch(arr, searchElement):
    for index in range(0, len(arr)):
        if arr[index] == searchElement:
            return index

arr = [17,23,45,76,89,12,32,67,-12]

print(linearSearch(arr = arr, searchElement = -12))