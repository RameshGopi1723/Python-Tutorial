# Check if given array is Monotonic
def isMonotonic(array):
    x, y = [], []
    x.extend(array)
    y.extend(array)
    x.sort()
    y.sort(reverse=True)
    if(x == array or y == array):
        return True
    return False


arr = [6, 5, 4, 1]

print(isMonotonic(arr))
