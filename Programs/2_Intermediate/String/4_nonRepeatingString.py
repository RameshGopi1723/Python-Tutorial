def nonRepeatingString(str):
    lst = []
    output = ""
    
    for char in str:
        if char not in lst:
            lst.append(char)
            output += char
    
    return lst, output
    

str = "Programming"

print(nonRepeatingString(str = str))