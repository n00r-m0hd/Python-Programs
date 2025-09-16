'''
1.capitalize() Capitalizes first letter of string

2.casefold() Converts all uppercase letters in string to lowercase. Similar to lower(), 
but works on UNICODE characters alos

3.lower() Converts all uppercase letters in string to lowercase.

4.swapcase() Inverts case for all letters in string.

5.title() Returns "titlecased" version of string, that is, 
all words begin with uppercase and the rest are lowercase.

6.upper()
Converts lowercase letters in string to uppercase.



'''

name = "python is a case sensitive language"

print(name.capitalize())

name = "Python is a dynamically typed language, It is ComPiled and InterPreted BOTH"

print(name.casefold())

name = "PYTHON IS EASY TO LEARN"

print(name.lower())

name = "python is an object oriented programming language"

print(name.upper())

name = "python can be used for web development, data science, and cyber security and much much more...."

print(name.title())

name = "i love python......"

print(name.swapcase())