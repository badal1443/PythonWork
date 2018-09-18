## Creating a function to check if a strng is a pelindrome
## To use this function import this file in other python files.
## Use import pelindrome in other python file.

def isPelindrome(string):
    string = string.lower()
    reversedStr = "".join(reversed(string))
    if reversedStr == string:
        return True
    return False


