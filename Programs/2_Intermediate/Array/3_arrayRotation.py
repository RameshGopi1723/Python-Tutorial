def leftRotateList(array, rotationElements, arrayLength):
    array[:]=array[rotationElements:arrayLength]+array[0:rotationElements]
    return array


def rightRotateList(array, rotationElements, arrayLenght):
    array[:] = array[-rotationElements:] + array[0:-rotationElements]
    return array


array = [1, 2, 3, 4, 5, 6]
rotationElements = 1


print("Original Array: ", array)

leftRotate = leftRotateList(array.copy(), rotationElements, len(array))
rightRotate = rightRotateList(array.copy(), rotationElements, len(array))

print("Left Rotated list is: ", leftRotate)
print("Right Rotated list is: ", rightRotate) 