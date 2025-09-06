# Write a program to calculate the factorial of a number

num = int(input("Enter an Integer\n"))

fact = 1
i = 1

while i<=num:
    fact = fact * i

    i += 1

print(f"Factorial of {num} is {fact}")
 