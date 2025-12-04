# Python program to split array and move first
def splitArrayAndAddEnd(array, splitPosition):
    x = array[:splitPosition]
    y = array[splitPosition:]
    y.extend(x)
    return y
    

arr = [12, 10, 5, 6, 52, 36]
splitPosition = 3

splitOutput = splitArrayAndAddEnd(arr.copy(), splitPosition)

print("Original array: ", arr)
print("Splitted and added array to the end: ",splitOutput)