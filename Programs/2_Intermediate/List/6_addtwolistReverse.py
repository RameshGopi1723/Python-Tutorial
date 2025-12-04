def addTwoNumbers(l1, l2):
    list1 = l1[::-1]
    list2 = l2[::-1]    
    list3 = []
    
    list1 = int(''.join(map(str, list1)))
    list2 = int(''.join(map(str, list2)))
    list = list1 + list2
    
    for digit in str(list):
        list3.append(int(digit))
    return list3
    

l1 = [2,4,3]
l2 = [5,6,4]

print(addTwoNumbers(l1,l2))