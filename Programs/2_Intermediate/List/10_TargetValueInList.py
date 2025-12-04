def targetValueInList(lst, target):
    output = []
    for i in range(0, len(lst)):
        print("outer loop: ",i)
        for j in range(i):
            print("inner loop: ", j)
            if lst[i] + lst[j] == target:
                output.append([lst[i],lst[j]])
    
    return output

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

print(targetValueInList(lst = lst, target = target))