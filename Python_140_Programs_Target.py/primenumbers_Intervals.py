# Write a program to check prime numbers in a given interval

lower = int(input("Enter the value of lower interval\n"))

upper = int(input("Enter the value of upper interval\n"))

"""
We can also assign the values of lower and upper interval like this
lower = 1
upper = 10
"""



print(f"Prime numbers between {lower} and {upper}")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(f"{num}")