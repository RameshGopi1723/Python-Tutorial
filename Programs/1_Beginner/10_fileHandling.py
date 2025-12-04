def fileFunction(filePath):
    with open(file = filePath, mode = 'r') as file:
        content = file.read()
        return content
    
user_input = input("Enter the file path to read file: ")
output = fileFunction(user_input)

print(output)
