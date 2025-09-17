#Strings are objects in Python, so they can be manipulated like any other object.
# Strings are immutable, meaning they cannot be changed after creation.
# Strings can be indexed, sliced, and iterated over like lists.
# Strings can be concatenated using the + operator.
# Strings can be formatted using f-strings or the format() method.
# Strings can be split into lists using the split() method.
# Strings can be joined using the join() method.
# Strings can be searched using the find() or index() methods.
# Strings can be converted to lowercase or uppercase using the lower() and upper() methods.
# Strings can be stripped of whitespace using the strip() method.
# Strings can be checked for membership using the in operator.
# Strings can be checked for equality using the == operator.
# Strings can be checked for inequality using the != operator.
# Strings can be checked for truthiness using the if statement.
# Strings can be checked for falsiness using the if not statement.
# Strings can be checked for length using the len() function.
# Strings can be checked for empty using the not operator.
# Strings can be checked for non-empty using the if statement.
# Strings can be checked for specific characters using the in operator.
# Strings can be checked for specific substrings using the in operator.
# Strings can be checked for specific prefixes using the startswith() method.
# Strings can be checked for specific suffixes using the endswith() method.
teststr = "Hello Python"

#uerate over string as a list of characters

index =0

while index < len(teststr):
    print(teststr[index])
    index+=1

for c in teststr:
    print(c)


#Slicing

print(teststr[0:5])

print(teststr[0:100]) # will work without throwing exception, but will return only the available characters.

print(teststr[:-1]) # skip last character

print(teststr[::-1]) # reverse the string
print(teststr[::2]) # skip every second character

print(teststr[3:5]) # get characters from index 3 to 5 (exclusive)

#find all methods associated with string
print(dir(teststr))
#help on string methods
#help(str)

print(teststr.find("Py")) # find returns the index of the first occurrence of the substring, or -1 if not found

teststr.replace("Python","Dunia")

str1 = "Hello"
str2 = "World"
# Concatenate strings
print(str1 + " " + str2)  # Using + operator