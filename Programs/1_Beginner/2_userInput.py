#getting the user input function
def userInput():
    name = input("Enter your name: ")
    greet = f"Hello {name}, Welcome..!"
    return greet


print(userInput())