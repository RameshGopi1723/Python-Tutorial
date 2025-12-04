def nonRepeatingString(str):
    count = {}
    
    for i in str:
        count[i] = count.get(i,0) + 1
    
    print(count)
        
    for index, char in enumerate(str):
        if count[char] == 1:
            return index
    
    return -1


str = "loveleetcode"
print(nonRepeatingString(str))