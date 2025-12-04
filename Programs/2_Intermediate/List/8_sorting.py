def sortList(lst):
    sorted_list = []
    
    while lst:
        max_val = max(lst)
        print("Current max: ", max_val)
        sorted_list.append(max_val)
        lst.remove(max_val)
        print("Sorted list so far: ", sorted_list)
        print("Remaining list: ", lst)
    
    output = sorted_list[::-1]
    return output



lst = [10,1,5,6,12,45,17,23]
print(sortList(lst=lst))