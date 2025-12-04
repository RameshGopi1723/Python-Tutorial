def zeroToEnd(lst):
    lst1 = []
    zeroCount = 0
    
    for i in lst:
        if i != 0:
            lst1.append(i)
        else:
            zeroCount += 1
            
    output = lst1 + ([0] * zeroCount)
    return output

lst = [1, 0, 2, 0, 0, 3,0,0,1,2,3,4,5,6,0,1]

print(zeroToEnd(lst=lst))