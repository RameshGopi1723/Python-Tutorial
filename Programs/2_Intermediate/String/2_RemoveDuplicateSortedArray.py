def removeDuplicates(nums):
    set1 = set()
    count = 0
    list = []
    
    for i in nums:
        set1.add(i)
    
    for i in set1:
        count+=1
        list.append(i)
    
    for i in range(len(nums)):
        if i in list:
            continue
        else:
            list.append("_")
    
    return count, list


count, list = removeDuplicates(nums=[1,2,2,3,4,4,4,5,5,5,5])

print("Count:",count, "List:",list) 