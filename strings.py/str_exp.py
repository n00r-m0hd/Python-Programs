'''

In Python, a string is an immutable sequence of Unicode characters.
Each character has a unique numeric value as per the UNICODE standard.
But, the sequence as a whole, doesn't have any numeric value even if all the characters are digits.
To differentiate the string from numbers and other identifiers, 
the sequence of characters is included within single, double or triple quotes in its literal representation. 
Hence, 1234 is a number (integer) but '1234' is a string.


string default slicing starts from index zero 
string default ending value is -1 

'''


name = "One day i will be in my field, InshaAllah"

print(name)

var="HELLO PYTHON"
print ("var:",var)
print ("var[-1:7]:", var[-1:7])
print ("var[7:0]:", var[7:0])


var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])


var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])


var="HELLO PYTHON"
print ("var:",var)
print ("var[0:12]:", var[0:12])
print ("var[:]:", var[:])