def listComp(start, stop):
    squares = [x**2 for x in range(start, stop) if x % 2 == 0]
    return squares


output = listComp(start = 4, stop = 15)
print(output)