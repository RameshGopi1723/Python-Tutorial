def sortDesc(array):
    swapped = False
    
    for i in range(len(array)-1, 0, -1):
        
        for j in range(i):    
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        
        if not swapped:
            break
    
    return array
           

array = [17,23,56,98,12,45]     
print(sortDesc(array))