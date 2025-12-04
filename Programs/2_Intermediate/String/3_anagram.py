def anagram(str1, str2):
    if len(str1) == len(str2):
        dict1 = {}
        dict2 = {}
        
        for char in str1:
            dict1[char] = dict1.get(char, 0)+1
            print(char, dict1)
        
        for char in str2:
            dict2[char] = dict2.get(char, 0)+1
            print(char, dict2)
        
        print(dict1, "==", dict2)
        return dict1 == dict2
        
    else:
        return False
    

str1 = "silent"
str2 = "listen"
print(anagram(str1 = str1, str2 = str2))


