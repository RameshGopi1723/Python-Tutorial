def is_Palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


text = input("Enter a string: ")

print("Text is Palindrome" if is_Palindrome(text) else "Text is Not a Palindrome" )
