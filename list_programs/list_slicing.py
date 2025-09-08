# Understanding the list slicing

'''
List Slicing

Syntax                  Description

lst[start:end]          Get sublist from index start to end-1
lst[:n]                 First n elements
lst[n:]                 From n to end
lst[::-1]               Reversed list

'''  

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[:5])
print(numbers[6:])
print(numbers[1:5])

print(numbers[2:6])

# If you want to reverse a list then simply write this statement

print(numbers[::-1])
