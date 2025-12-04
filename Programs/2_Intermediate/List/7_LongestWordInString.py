

def longestWordString(str="aked kajdfl"):
    dict = {}
    count = 0
    
    splittedString = str.split(" ")
    print("splittedString:", splittedString)
    for i in splittedString:
        for j in i:
            count += 1
        dict.update({i:count})
        count = 0
    
    max_value = 0
    max_key = ""
    for key, value in dict.items():
        if max_value > dict[key]:
            max_value = dict[key]
            max_key = value
            
    
    return max_value, max_key
    
    # return max(dict, key = dict.get)
    

print(longestWordString(str = "Gopinath R"))