## Creating a function to check if a strng is a palindrome
## To use this function import this file in other python files.
## Use import palindrome in other python file.

def isPalindrome(string):
    string = string.lower()
    reversedStr = "".join(reversed(string))
    if reversedStr == string:
        return True
    return False


