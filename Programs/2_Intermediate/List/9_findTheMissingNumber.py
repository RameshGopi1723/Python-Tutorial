def missingNumber(lst):
    
    for i in range(len(lst) + 1):
        if i not in lst:
            return i

# Test case
lst = [9,6,4,2,3,5,7,0,1,8,11,10]
print(missingNumber(lst)) 
