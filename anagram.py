## Find if two strings are anagrams of each other
def is_anagram(str1,str2):
    placeholder = list(str1)
    if len(str1) != len(str2):
        return False
    str2=list(str2)
    for c in str1:
        try:
            str2.remove(c)
        except ValueError:
            return False
        placeholder.remove(c)
    if len(str2) == 0 and len(placeholder) == 0:
        return True
    else:
        return False
    

if (is_anagram("me","pe")):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")   