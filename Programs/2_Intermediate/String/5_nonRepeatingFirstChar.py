def nonRepeatingFirstChar(str):
    dict = {}
    
    for char in str:
        dict[char] = dict.get(char, 0) + 1
        print(dict)
    
    for char in str:
        if dict[char] == 1:
            return char 
    
    return "No Non-Repeating Char"



str = "Krishnaveni"

print(nonRepeatingFirstChar(str = str))