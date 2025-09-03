'''
Triple Sum with Equality Rule
Write a Python program to sum three given integers.
However, if two values are equal, the sum will be zero.
'''

a=int(input("Enter the value of a\n"))
b=int(input("Enter the value of b\n"))
c=int(input("Enter the value of c\n"))

sum = a+b+c
print(f"Sum of {a} , {b} , and {c} is {sum}")

if(a==b or a==c or b==a or b==c or c==a or c==b):
    sum=0
    print(f"Now sum is {sum}")

else:
    print(f"The given values of {a} , {b} , and {c} are not equal or different")