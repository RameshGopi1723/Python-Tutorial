def dictValue(dict, dictKey):
    value = dict.get(dictKey)
    return value

marks = {"John": 85, "Alice": 90, "Bob": 78}
name = input("Enter student name: ")
print("Marks:", dictValue(marks, name))
