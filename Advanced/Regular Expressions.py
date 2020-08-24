# A RegEx, or Regular Expression, is a sequence of characters that forms a
# search pattern. RegEx can be used to check if a string contains the
# specified search pattern.

# Useful websites:
# https://www.dataquest.io/blog/regex-cheatsheet/
# https://www.debuggex.com/cheatsheet/regex/python
# https://docs.python.org/3/library/re.html

# Python has a built-in package called re, which can be used to work with
# Regular Expressions.
import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

# Search for the first white-space character in the string:
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())

# Split at each white-space character:
x = re.split("\s", str)
print(x)

# Split the string only at the first occurrence:
x = re.split("\s", str, 1)
print(x)

# Replace every white-space character with the number 9:
x = re.sub("\s", "9", str) 
print(x)

# Replace the first 2 occurrences:
x = re.sub("\s", "9", str, 2) 
print(x)

# A Match Object is an object containing information about the search
# and the result.
# looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", str)
print(x) #this will print an object

# The Match object has properties and methods used to retrieve information
# about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
print(x.span())
# .string returns the string passed into the function
print(x.string)
# .group() returns the part of the string where there was a match
print(x.group())

